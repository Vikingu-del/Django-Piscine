$(document).ready(function() {
    const roomName = JSON.parse($('#room-name').text());
    const currentUsername = JSON.parse($('#user-username').text());
    const wsScheme = window.location.protocol === "https:" ? "wss" : "ws";
    const wsUrl = `${wsScheme}://${window.location.host}/ws/chat/${roomName}/`;
    const chatSocket = new WebSocket(wsUrl);
    const $chatLog = $('#chat-log');
    const $userList = $('#user-list');
    const $messageInput = $('#chat-message-input');

    function appendChatMessage(username, message) {
        const isMe = username === currentUsername;
        const alignment = isMe ? 'align-self-end bg-primary text-white' : 'align-self-start bg-white text-dark border';

        $chatLog.append(`
            <div class="p-2 my-1 rounded shadow-sm ${alignment}" style="max-width: 75%;">
                <small class="fw-bold d-block ${isMe ? 'text-white-50' : 'text-muted'}">${username}</small>
                <span>${message}</span>
            </div>
        `);
    }

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const action = data.action;
        const payload = data.payload;

        if (action === "room_history") {
            $chatLog.empty(); 
            if (payload && Array.isArray(payload.messages)) {
                payload.messages.forEach(function(msg) {
                    appendChatMessage(msg.username, msg.message);
                });
            }
        } else if (action === 'system_alert') {
            $chatLog.append(`
                <div class="text-center my-2">
                    <span class="badge bg-secondary text-wrap">${payload.message}</span>
                </div>
            `);
        } else if (action === 'chat_message' || action === 'receive_chat_message') {
            appendChatMessage(payload.username, payload.message);
        } else if (action === 'user_list') {
            $userList.empty();
            if (payload.users && Array.isArray(payload.users)) {
                payload.users.forEach(user => {
                    const isMe = user === currentUsername;
                    $userList.append(`
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                            ${user} ${isMe ? '<span class="badge bg-primary rounded-pill">You</span>' : ''}
                        </li>
                    `);
                });
            }
        }
    };

    function sendMessage() {
        const text = $messageInput.val().trim();
        if (text !== '') {
            chatSocket.send(JSON.stringify({
                action: "send_message",
                payload: { message: text }
            }));
            $messageInput.val('');
        }
    }

    $(document).on('click', '#chat-message-submit', function(e) {
        e.preventDefault();
        sendMessage();
    });

    $messageInput.on('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            sendMessage();
        }
    });
});
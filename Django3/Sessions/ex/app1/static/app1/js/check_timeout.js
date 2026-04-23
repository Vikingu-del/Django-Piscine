setInterval(function() {
    fetch(window.location.href)
        .then(response => response.text())
        .then(html => {
            // Create a temporary element to parse the new HTML
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const newName = doc.getElementById('user-name').innerText;
            const currentName = document.getElementById('user-name').innerText;
            
            // If the server gave us a different name, update it instantly!
            if (newName !== currentName) {
                document.getElementById('user-name').innerText = newName;
            }
        });
}, 1000);
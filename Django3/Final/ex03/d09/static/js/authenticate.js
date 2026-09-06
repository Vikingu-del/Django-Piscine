function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            let csrfToken = $('input[name="csrfmiddlewaretoken"]').val() || getCookie('csrftoken');
            if (csrfToken) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        }
    }
});

$(() => {
    // ==========================================
    // 1. HANDLE THE LOGIN FORM
    // ==========================================
    $('#ajax-auth-form').on('submit', function(event) {
        event.preventDefault();

        // Hide the error box and clear old text when submitting again
        $('#login-errors').addClass('d-none').empty();

        let $form = $(this);
        let formData = $form.serialize();

        $.ajax({
            url: $form.attr('action'),
            type: $form.attr('method'),
            data: formData,
            dataType: 'json',
        })
        .done(function(response) {
            if (response.success) {
                $('#current-username').text(response.username);
                $('#login-section').addClass('d-none');
                $('#logout-section').removeClass('d-none');
                $('#id_password').val('');
                if (response.csrf_token) {
                    $('input[name="csrfmiddlewaretoken"]').val(response.csrf_token);
                    document.cookie = "csrftoken=" + response.csrf_token + "; path=/;";
                }
            }
        })
        .fail(function(xhr) {
            let response = xhr.responseJSON || {};
            let errorMsg = response.error;

            if (response.errors && response.errors.__all__) {
                errorMsg = response.errors.__all__[0];
            }

            if (!errorMsg) {
                errorMsg = 'An error occurred. Please try again.';
            }

            $('#login-errors').removeClass('d-none').text(errorMsg);
        });
    })
    // ==========================================
    // 2. HANDLE THE LOGOUT BUTTON
    // ==========================================
    $('#ajax-logout-btn').on('click', function() {
        $.ajax({
            url: $(this).data('url'),
            type: 'POST',
        })
        .done(function(response) {
            if (response.success) {
                $('#current-username').text('');
                $('#logout-section').addClass('d-none');
                $('#login-section').removeClass('d-none');
            }
        })
        .fail(function(xhr) {
            console.error('Logout failed:', xhr.responseText);
        });
    })
});

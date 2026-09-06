$(document).ready(function() {
    // ==========================================
    // 1. HANDLE THE LOGIN FORM
    // ==========================================
    $('#ajax-auth-form').on('submit', function(event) {
        event.preventDefault();

        // Hide the error box and clear old text when submitting again
        $('#login-errors').addClass('d-none').empty();

        let formData = $(this).serialize();

        $.ajax({
            url: 'login/',
            type: 'POST',
            data: formData,
            success: function(response) {
                if (response.success) {
                    $('#current-username').text(response.username);
                    $('#login-section').addClass('d-none');
                    $('#logout-section').removeClass('d-none');
                    $('#id_password').val('');
                }
            },
            error: function(xhr) {
                let response = xhr.responseJSON;
                let errorMsg = response.error || 'An error occurred. Please try again.';

                if (response && response.errors && response.errors.__all__) {
                    errorMsg = response.errors.__all__[0];
                }

                $('#login-errors').removeClass('d-none').text(errorMsg);
            }
        })
    })
    // ==========================================
    // 2. HANDLE THE LOGOUT BUTTON
    // ==========================================
    $('#ajax-logout-btn').on('click', function() {
        let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: 'logout/',
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrfToken
            },
            success: function(response) {
                if (response.success) {
                    $('#current-username').text('');
                    $('#logout-section').addClass('d-none');
                    $('#login-section').removeClass('d-none');
                }
            },
            error: function() {
                alert('An error occurred while logging out. Please try again.');
            }
        });
    })
});

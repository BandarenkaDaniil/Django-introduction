function loginUser(event) {
    let loginForm = $("#loginForm");

    let submitButton = loginForm.find(':submit');
    submitButton.attr('disabled', 'disabled');

    let loadingSpan = $("<span></span>");
    loadingSpan.attr('class', 'spinner-border spinner-border-sm');

    submitButton.text(' Loading...');
    submitButton.prepend(loadingSpan);

    event.preventDefault();
    $.post(
        LOGIN_URL,
        loginForm.serialize(),
        function (data) {
            let auth_token = JSON.parse(data).token;

            setCookie(
                'Authorization',
                'Token ' + auth_token,
                2
            );

            location.reload();
        },
        'text'
    ).fail(
        () => {
            submitButton.removeAttr('disabled');
            submitButton.text('Submit');

            shake($("#loginModal"));
        }
    );
}
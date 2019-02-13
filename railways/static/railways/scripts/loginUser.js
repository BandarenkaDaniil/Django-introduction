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
        (response) => {
            let errors = JSON.parse(response.responseText);

            $('#loginForm').find('input').removeClass(
                'is-invalid'
            );

            Object.entries(errors).map(entry => {
                let errorInput = $(`#${entry[0]}`);

                errorInput.addClass('is-invalid');

                errorInput.next().text(entry[1]);
            });

            submitButton.removeAttr('disabled');
            submitButton.text('Submit');

            shake($("#loginModal"));
        }
    );
}
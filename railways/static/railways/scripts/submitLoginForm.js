function submitLoginForm(event) {
    let loginForm = $("#login_form");

    event.preventDefault();
    $.post(
        '/api/users/login/',
        loginForm.serialize(),
        function (data) {
            let auth_token = JSON.parse(data).token;

            setCookie('Authorization', 'Token ' + auth_token, 2);

            loginForm.hide();
            $("#data_specifying_form").show();
        },
        'text'
    ).fail(
        () => alert('Incorrect data')
    );
}
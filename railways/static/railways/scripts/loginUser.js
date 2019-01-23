function loginUser(event) {
    let loginForm = $("#loginForm");

    event.preventDefault();
    $.post(
        '/api/users/login/',
        loginForm.serialize(),
        function (data) {
            let auth_token = JSON.parse(data).token;

            setCookie('Authorization', 'Token ' + auth_token, 2);

            loginForm.hide();
            $("#dataSpecifyingForm").show();
        },
        'text'
    ).fail(
        () => alert('Incorrect data')
    );
}
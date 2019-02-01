function logout(event) {
    let auth_token = getCookie('Authorization');

    $.ajaxSetup({
        headers: {
            'Authorization': auth_token
        }
    });

    $.post(
        LOGOUT_URL,
        function (data) {
            setCookie('Authorization', '', -1);
            location.reload();
        },
        'text'
    ).fail(
        () => {
            setCookie('Authorization', '', -1);
            location.reload();
        }
    );
}
function logout(event) {
    let auth_token = getCookie('Authorization');

    $.ajaxSetup({
        headers: {
            'Authorization': auth_token
        }
    });

    $.post(
        '/api/users/logout/',
        function (data) {
            setCookie('Authorization', '', -1);
        },
        'text'
    ).fail(
        () => alert('Cannot log out')
    );
}
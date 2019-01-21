function getUserTickets(event) {
    let auth_token = getCookie('Authorization');

    $.ajaxSetup({
        headers: {
            'Authorization': auth_token
        }
    });

    $.get(
        '/api/railways/user_tickets/',
        function (data) {
            let str = '<ul>';

            for (let i = 0; i < data.length; i++) {
                str += '<li>'
                    + Object.values(data[i]).join('-')
                    + '</li>';
            }
            str += '</ul>';

            $('#modal-trains pre').html(str);
        },
        'json'
    ).fail(
        function () {
           alert('user tickets request failed');
        }
    );
}
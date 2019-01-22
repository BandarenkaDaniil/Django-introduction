function buyTicket(event) {
    let data = {
        ride_id: event['target'].getAttribute('data-ride-id')
    };

    let auth_token = getCookie('Authorization');

    $.ajaxSetup({
        headers: {
            'Authorization': auth_token
        }
    });

    $.post(
        '/api/railways/buy_ticket/',
        data,
        function (data) {
            alert('Purchased');
        },
        'json'
    ).fail(
        function () {
           alert('ticket purchase failed'); // or whatever
        }
    );
}
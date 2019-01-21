function buyTicket(event) {
    let inputs = event['target'].innerHTML.split(' ');

    let data = {
        departure_station: inputs[1],
        arrival_station: inputs[2],
        departure_date: inputs[3],
        departure_time: inputs[5]
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
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
            let str = '<table class="table table-hover">';
            str += '<thead><tr><th>From</th><th>To</th><th>Departure date</th><th>Arrival date</th><th>Departure time</th><th>Arrival time</th></tr></thead>';
            str += '<tbody>';

            for (let i = 0; i < data.length; i++) {
                str += '<tr>';

                str += `<td>${data[i].departure_station}</td>
                        <td>${data[i].arrival_station}</td>
                        <td>${data[i].departure_date}</td>
                        <td>${data[i].arrival_date}</td>
                        <td>${data[i].departure_time}</td>
                        <td>${data[i].arrival_time}</td>`;

                str += '</tr>';
            }

            str += '</tbody></table>';

            $('#modal-trains pre').html(str);
        },        'json'
    ).fail(
        function () {
            let str = '<div class="list-group">';

            str += 'You haven\'t got any tickets';

            str += '</div>';

            $('#modal-trains pre').html(str);
        }
    );
}
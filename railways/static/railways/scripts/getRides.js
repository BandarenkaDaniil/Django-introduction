function getRides() {
    let auth_token = getCookie('Authorization');

    $.ajaxSetup({
        headers: {
            'Authorization': auth_token
        }
    });

    $.get(
        '/api/railways/ride/',
        dataSpecifyingForm.serialize(),
        function (data) {
            let str = '<table class="table table-hover">';
            str += '<thead><tr><th>From</th><th>To</th><th>Departure date</th><th>Arrival date</th><th>Departure time</th><th>Arrival time</th><th>Price</th></tr></thead>';
            str += '<tbody>';

            for (let i = 0; i < data.length; i++) {
                str += '<tr class="rides-table-row">';

                str += `<td>${data[i].departure_station}</td>
                        <td>${data[i].arrival_station}</td>
                        <td>${data[i].departure_date}</td>
                        <td>${data[i].arrival_date}</td>
                        <td>${data[i].departure_time}</td>
                        <td>${data[i].arrival_time}</td>
                        <td>${data[i].amount}</td>
                        <td><button type="button" class="btn btn-primary btn-sm btn-buy-ticket" data-ride-id="${data[i].id}">Buy</button></td>`;

                str += '</tr>';
            }
            str += '</tbody></table>';

            $('#trains pre').html(str);
        },
        'json'
    ).fail(
        function () {
            let str = '<h2>Rides</h2>';
            str += '<div class="list-group">';

            str += 'No rides for this data';

            str += '</div>';

            $('#trains pre').html(str);
        }
    );
}
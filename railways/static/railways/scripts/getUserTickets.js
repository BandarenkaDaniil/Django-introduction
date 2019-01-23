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
            let table = document.createElement('table');
            table.setAttribute('class', 'table table-hover');

            let tableHead = document.createElement('thead');
            let columnHeaders = [
                'From',
                'To',
                'Departure date',
                'Arrival date',
                'Departure time',
                'Arrival time'
            ];

            for (let i = 0; i < columnHeaders.length; i++) {
                let columnHeaderElem = document.createElement('th');
                let headerText = document.createTextNode(columnHeaders[i]);

                columnHeaderElem.appendChild(headerText);
                tableHead.appendChild(columnHeaderElem);
            }
            table.appendChild(tableHead);

            let tableBody = document.createElement('tbody');

            for (let i = 0; i < data.length; i++) {

                let tableRow = document.createElement('tr');

                let rowValues = [
                    data[i].departure_station,
                    data[i].arrival_station,
                    moment(data[i].departure_date).format("MMM Do YYYY"),
                    moment(data[i].departure_date).format("MMM Do YYYY"),
                    data[i].departure_time,
                    data[i].arrival_time
                ];

                for (let k = 0; k < rowValues.length; k++) {
                    let rowCell = document.createElement('td');

                    let cellText = document.createTextNode(rowValues[k]);

                    rowCell.appendChild(cellText);
                    tableRow.appendChild(rowCell);
                }

                tableBody.appendChild(tableRow);
            }

            table.appendChild(tableBody);

            let trains = document.getElementById('trainsModalBody');
            while (trains.firstChild) {
                trains.removeChild(trains.firstChild)
            }
            trains.appendChild(table);
        },
        'json'
    ).fail(
        function () {
            let str = '<div class="list-group">';

            str += 'You haven\'t got any tickets';

            str += '</div>';

            $('#modal-trains pre').html(str);
        }
    );
}
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
            let table = document.createElement('table');
            table.setAttribute('class', 'table table-hover');

            let tableHead = document.createElement('thead');
            let columnHeaders = [
                'From',
                'To',
                'Departure date',
                'Arrival date',
                'Departure time',
                'Arrival time',
                'Price',
                'Buy'
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
                    data[i].arrival_time,
                    data[i].amount
                ];

                for (let k = 0; k < rowValues.length; k++) {
                    let rowCell = document.createElement('td');
                    rowCell.setAttribute('class', 'align-middle');

                    let cellText = document.createTextNode(rowValues[k]);

                    rowCell.appendChild(cellText);
                    tableRow.appendChild(rowCell);
                }

                let button = document.createElement('button');
                button.setAttribute('type', 'button');
                button.setAttribute('class', 'btn btn-primary btn-sm btn-buy-ticket');
                button.setAttribute('data-ride-id', data[i].id);

                let buttonText = document.createTextNode('Buy');

                let buttonCell = document.createElement('td');
                button.appendChild(buttonText);
                buttonCell.appendChild(button);
                tableRow.appendChild(buttonCell);

                tableBody.appendChild(tableRow);
            }

            table.appendChild(tableBody);

            let trains = document.getElementById('trains');
            while (trains.firstChild) {
                trains.removeChild(trains.firstChild)
            }
            trains.appendChild(table);
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
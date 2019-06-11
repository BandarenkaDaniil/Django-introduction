function getRides(event) {
    event.preventDefault();

    let auth_token = getCookie('Authorization');

    $.ajaxSetup({
        headers: {
            'Authorization': auth_token
        }
    });

    let dataSpecifyingForm = $('#dataSpecifyingForm');
    let submitButton = dataSpecifyingForm.find(':submit');
    submitButton.attr('disabled', 'disabled');

    let loadingSpan = $("<span></span>");
    loadingSpan.attr('class', 'spinner-border spinner-border-sm');

    submitButton.text(' Loading...');
    submitButton.prepend(loadingSpan);

    $.get(
        RIDE_URL,
        dataSpecifyingForm.serialize(),
        function (data) {
            let table = document.createElement('table');
            table.setAttribute('class', 'table table-hover');

            let tableHead = document.createElement('thead');
            let columnHeaders = [
                'Departure',
                'Arrival',
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
                    data[i].departure_time,
                    moment(data[i].arrival_date).format("MMM Do YYYY") + '\n' +
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
                button.setAttribute(
                    'class',
                    'btn btn-primary btn-sm btn-buy-ticket'
                );
                button.setAttribute('data-ride-id', data[i].id);

                let buttonText = document.createTextNode('Buy');

                let buttonCell = document.createElement('td');
                button.appendChild(buttonText);
                buttonCell.appendChild(button);
                tableRow.appendChild(buttonCell);

                let link = document.createElement('a');
                link.setAttribute(
                    'href',
                    '#collapse' + i
                );
                link.setAttribute(
                    'class',
                    'collapsed card-link'
                );
                link.setAttribute('data-toggle', 'collapse');

                let arrow = document.createElement('i');
                arrow.setAttribute(
                    'class',
                    'material-icons'
                );

                let arrowText = document.createTextNode(
                    'keyboard_arrow_down'
                );
                arrow.appendChild(arrowText);

                link.appendChild(arrow);

                let linkCell = document.createElement('td');
                linkCell.appendChild(link);
                tableRow.appendChild(linkCell);

                let collapseDiv = document.createElement('div');
                collapseDiv.setAttribute(
                    'id',
                    'collapse' + i
                );
                collapseDiv.setAttribute(
                    'class',
                    'collapse'
                );
                collapseDiv.setAttribute(
                    'data-parent',
                    '#trains'
                );

                let collapseElem = generateRideInfoCollapse(data[i].items);

                collapseDiv.appendChild(collapseElem);

                tableBody.appendChild(tableRow);
                tableBody.appendChild(collapseDiv);
            }

            table.appendChild(tableBody);

            let trains = document.getElementById('rides');
            while (trains.firstChild) {
                trains.removeChild(trains.firstChild)
            }
            trains.appendChild(table);

            submitButton.removeAttr('disabled');
            submitButton.text('Choose');

            $("#ridesDiv").show();
        },
        'json'
    ).fail(
        (response) => {
            let errors = JSON.parse(response.responseText);

            $('#dataSpecifyingForm').find('input').removeClass(
                'is-invalid'
            );

            Object.entries(errors).map(entry => {
                let errorInput = $(`#${entry[0]}`);

                errorInput.addClass('is-invalid');

                errorInput.next().text(entry[1]);
            });

            submitButton.removeAttr('disabled');
            submitButton.text('Choose');

            shake($("#dataSpecifyingDiv"));
        }
    );

}
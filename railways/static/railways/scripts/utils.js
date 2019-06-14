function getCookie(cookieName) {
    let name = cookieName + "=";
    let cookieArray = document.cookie.split(';');

    for (let i = 0; i < cookieArray.length; i++) {
        let c = cookieArray[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }

    return "";
}

function setCookie(name, value, expireDays) {
    let date = new Date();

    date.setTime(date.getTime() + (expireDays * 24 * 60 * 60 * 1000));

    let expires = "expires=" + date.toUTCString();

    document.cookie = name + '=' + value + ';' + expires;
}

function generateAlert(message, alertType) {
    let alert = $('<div></div>');
    alert.attr(
        'class',
        'alert alert-dismissible' + ' ' + alertType
    );

    let dismissButton = $('<button></button>');
    dismissButton.attr('type', 'button');
    dismissButton.attr('class', 'close');
    dismissButton.attr('data-dismiss', 'alert');

    dismissButton.text('×');
    alert.text(message);
    alert.append(dismissButton);

    return alert;
}

function generateRideInfoCollapse(items) {
    let container = document.createElement('div');
    container.setAttribute('class', 'container');

    let list = document.createElement('ul');
    list.setAttribute('class', 'list-group');

    for (let i = 0; i < items.length; i++) {
        let listItem = document.createElement('li');

        if (i === 0) {
            listItem.setAttribute(
                'class',
                'list-group-item list-group-item-success'
            );
        } else {
            listItem.setAttribute(
                'class',
                'list-group-item list-group-item-dark'
            );
        }

        let itemText = document.createTextNode(items[i].departure_station);

        listItem.appendChild(itemText);
        list.appendChild(listItem);

        if (i === items.length - 1) {
            let lastListItem = document.createElement('li');

            lastListItem.setAttribute(
                'class',
                'list-group-item list-group-item-danger'
            );

            let lastItemText = document.createTextNode(
                items[i].arrival_station
            );

            lastListItem.appendChild(lastItemText);
            list.appendChild(lastListItem);
        }
    }

    container.appendChild(list);

    return container;
}


function shake(elem) {
    const TIMES = 4;
    const SHIFT_SIZE = 30;
    const SHAKE_SPEED = 100;

    let direction = 1;

    for (let i = 0; i < TIMES; i++) {
        let sign = (direction === 1) ? '+' : '-';

        elem.animate({
                left: `${sign}=${SHIFT_SIZE}px`,
            },
            SHAKE_SPEED
        );

        direction *= -1;
    }
}

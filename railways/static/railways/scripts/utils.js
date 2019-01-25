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
    let d = new Date();

    d.setTime(d.getTime() + (expireDays * 24 * 60 * 60 * 1000));

    let expires = "expires=" + d.toUTCString();

    document.cookie = name + '=' + value + ';' + expires;
}

function generateAlert(message, alertType) {
    let alert = $('<div></div>');
    alert.attr('class', 'alert alert-dismissible' + ' ' + alertType);

    let dismissButton = $('<button></button>');
    dismissButton.attr('type', 'button');
    dismissButton.attr('class', 'close');
    dismissButton.attr('data-dismiss', 'alert');

    dismissButton.text('×');
    alert.text(message);
    alert.append(dismissButton);

    return alert;
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
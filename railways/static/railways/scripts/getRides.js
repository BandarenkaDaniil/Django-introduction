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
            let str = '<h2>Rides</h2>';
            str += '<div class="list-group">';

            for (let i = 0; i < data.length; i++) {

                str += '<a href="#" class="list-group-item list-group-item-action">'
                    + Object.values(data[i]).join(' ')
                    + '</a>';

            }
            str += '</div>';

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
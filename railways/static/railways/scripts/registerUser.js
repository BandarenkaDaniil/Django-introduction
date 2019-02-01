function registerUser(event) {
    let registerForm = $('#registerForm');

    let submitButton = registerForm.find(':submit');
    submitButton.attr('disabled', 'disabled');

    let loadingSpan = $("<span></span>");
    loadingSpan.attr('class', 'spinner-border spinner-border-sm');

    submitButton.text(' Loading...');
    submitButton.prepend(loadingSpan);

    event.preventDefault();
    $.post(
        USER_URL,
        registerForm.serialize(),
        function (data) {
            let message =
                'Success! You will be now redirected to the home page!';

            let alert = generateAlert(message, 'alert-success');

            $('.card-body').find('.messages').prepend(alert);

            setTimeout(
                () => {
                    document.location.replace('/');
                },
                3000);
        },
        'text'
    ).fail(
        (data) => {
            let responseText = JSON.parse(data['responseText']);

            let values = Object.values(responseText);
            let keys = Object.keys(responseText);

            for (let i = 0; i < values.length; i++) {
                let input = $(`input[name=${keys[i]}]`);
                console.log(values[i]);
                input.tooltip({
                    'trigger':'hover',
                    'title': values[i].join(',')});
                // input.attr('class', 'form-control is-invalid');

            }

            let message =
                'Invalid input. Point highlighted inputs to get more info.';

            let alert = generateAlert(message, 'alert-danger');

            $('.card-body').find('.messages').empty().prepend(alert);

            submitButton.removeAttr('disabled');
            submitButton.text('Submit');

            shake($("#registerDiv"));
        }
    );
}
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
        (response) => {
            let errors = JSON.parse(response['responseText']);

            $('#registerForm').find('input').removeClass(
                'is-invalid'
            );

            Object.entries(errors).map(entry => {
                let errorInput = $(`#${entry[0]}`);

                errorInput.addClass('is-invalid');

                errorInput.next().text(entry[1]);
            });

            submitButton.removeAttr('disabled');
            submitButton.text('Submit');

            shake($("#registerDiv"));
        }
    );
}
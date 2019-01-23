function registerUser(event) {
    let registerForm = $("#registerForm");

    event.preventDefault();
    $.post(
        '/api/users/',
        registerForm.serialize(),
        function (data) {
            console.log(data);
            document.location.replace('/');
        },
        'text'
    ).fail(
        () => alert('Incorrect data')
    );
}
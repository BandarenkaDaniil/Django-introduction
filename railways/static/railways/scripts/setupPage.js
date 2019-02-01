function setupPage() {
    $("#cartNavButton").on(
        "click",
        getUserTickets
    );

    $("#dataSpecifyingForm").on(
        "submit",
        getRides
    );

    $("#rides").on(
        'click',
        '.btn-buy-ticket',
        buyTicket
    );

    if (getCookie('Authorization') === '') {
        $("#loginForm").on(
            "submit",
            loginUser
        );

        $('#loginNavButton').show();
    } else {
        $('#dataSpecifyingDiv').show();

        $('#cartNavButton').show();

        $('#logoutNavButton').show().on(
            'click',
            logout
        )
    }
}
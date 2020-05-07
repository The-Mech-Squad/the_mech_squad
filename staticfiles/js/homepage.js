$(document).ready(function () {
    $('#search-button').click(function (e) {
        e.preventDefault();
        // get the nickname
        var sat_id = $(this).val();
        // GET AJAX request
        $.ajax({
            type: 'GET',
            url: "{% url 'find_sat' %}",
            data: {
                "sat_name": sat_id
            },
            success: function (response) {
                // if not valid satellite, alert the user
                if (!response["valid"]) {
                    alert("This Satellite doesn't exist");
                }
            },
            error: function (response) {
                console.log(response)
            }
        })
        // Search database for document.getElementById('search-box').val

        // Sending the 'id' of the sat back to Django through Ajax.
        // Django 'posts' to itself, realizes it is an AJAX call and calls the AJAX function
        // Django see's that the action is 'find sat' and executes if statement
        // Django calls find sat script using the id we sent
        // Selects TLE0,1,2 from db for that sat ID
        // converts tle to czml
        // returns czml
        // Django sends this czml to the page
        // JQuery updates the page using the passed information.

    });
})

/**
 * Created by Haoran on 2015-07-02.
 */
$("#updateuser-form").submit(function(event) {
    event.preventDefault();
    clickedUpdate();
});

function setLog(r) {
    $("#log").html(r);
}

function clickedUpdate() {
    setLog("Please wait...");
    $("#update-button").attr("disabled", "disabled");
    $.ajax({
        url: getImportUrL(),
        type: "POST",
        data: {
            csrfmiddlewaretoken: getCsrfToken()
        },
        //dataType: 'json',
        success: function() {
            setLog("Success!");
            $("#update-button").removeAttr("disabled");

            for (var i in users) {
                //$('#print_users').append(i. + '<br/>');
                setLog("print_users!");
        }

        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);

            setLog("Error! " + errorThrown);
            $("#update-button").removeAttr("disabled");
        }
    });
    return false;
}
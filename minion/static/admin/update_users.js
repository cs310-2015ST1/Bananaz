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
        url: getImportUrl(),
        type: "POST",
        data: {
            csrfmiddlewaretoken: getCsrfToken()
        },
        success: function() {
            setLog("Success!");
            $("#update-button").removeAttr("disabled");
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);

            setLog("Error! " + errorThrown);
            $("#update-button").removeAttr("disabled");
        }
    })
}
$("#post-form").submit(function(event) {
    event.preventDefault();
    clickedImport();
});

function setResult(r) {
    $("#results").html(r);
}
function clickedImport() {
    setResult("Please wait...");
    $("#submit-button").attr("disabled", "disabled");
    $.ajax({
        url: getImportUrl(),
        type: "POST",
        data: {
            csrfmiddlewaretoken: getCsrfToken()
        },
        success: function() {
            setResult("Success!");
            $("#submit-button").removeAttr("disabled");
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);

            setResult("Error! " + errorThrown);
            $("#submit-button").removeAttr("disabled");
        }
    })
}
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
        url: "http://127.0.0.1:8000/admin/import/",
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

            setResult("Error!  status: " + textStatus + "error: " + errorThrown);
            $("#submit-button").removeAttr("disabled");
        }
    })
}
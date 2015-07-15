function doAjaxCall(url, csrfToken, data, successCallback, failureCallback) {
    data = data || {};
    data.csrfmiddlewaretoken = csrfToken;

    $.ajax({
        url: url,
        type: "POST",
        data: data,
        success: function() {
            if(successCallback) {
                successCallback();
            }
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);

            if(failureCallback) {
                failureCallback();
            }
        }
    })
}
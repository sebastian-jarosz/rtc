$("#learnModels").click(function() {
    // Check if file was chosen
    var doNotMapData = $("#doNotMapData").is(":checked")

    var formData = new FormData()
    formData.append('doNotMapData', doNotMapData)

    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    formData.append('csrfmiddlewaretoken', csrf_token)

    $.ajax({
        type: 'POST',
        cache: false,
        contentType: false,
        processData: false,
        timeout: 500000,
        data: formData,
        processData: false,
        url: "/admin/api/teach/",
        // shows the spinner element before sending.
        beforeSend: function() {
            $("#learnModels").hide();
            $("#learnModelsSpinner").show();
        },
        // hides the spinner after completion of request, whether successfull or failor.
        complete: function() {
            $("#learnModelsSpinner").hide();
            $("#learnModels").show();
        },
        success: function(data) {
            $("#learnModelsSuccess").show();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $("#learnModelsError").show();
        },
    })
});
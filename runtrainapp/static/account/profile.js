// this is the id of the form
$("#stravaApi").click(function(e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.

    // init FormData
    var formData = new FormData()

    // Without token file will not be uploaded
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();


    formData.append('csrfmiddlewaretoken', csrf_token)

    $.ajax({
        type: "POST",
        cache: false,
        contentType: false,
        processData: false,
        timeout: 50000,
        data: formData,
        url: '/accounts/api/strava/',
        // shows the spinner element before sending.
        beforeSend: function() {
            $("#stravaApi").hide();
            $("#stravaApiSpinner").show();
        },
        // hides the spinner after completion of request, whether successfull or failor.
        complete: function() {
            $("#stravaApiSpinner").hide();
            $("#stravaApi").show();
        },
        success: function(data) {
            $("#stravaApiSuccess").show();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $("#stravaApiError").show();
        },
    });

});
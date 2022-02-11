$("#parseResponses").click(function() {
    // Check if file was chosen
    var responsesFileLen = document.getElementById("responsesFile").files.length
    if(responsesFileLen == 0) {
        // TODO pretty alert
        alert('Należy wybrać plik przed rozpoczęciem przesyłania!')
        return;
    }

    // init FormData
    var formData = new FormData()

    // Without token file will not be uploaded
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    formData.append('csrfmiddlewaretoken', csrf_token)

    // files key used for django purposes
    var responsesFile = document.getElementById("responsesFile").files[0]
    if(responsesFile.type != 'text/csv') {
        // TODO pretty alert
        alert('Wybrany plik musi być w formacie CSV!')
        return;
    }

    formData.append('files', responsesFile)

    $.ajax({
        type: 'POST',
        cache: false,
        contentType: false,
        processData: false,
        timeout: 500000,
        data: formData,
        processData: false,
        url: "/admin/api/parse/",
        // shows the spinner element before sending.
        beforeSend: function() {
            $("#parseResponses").hide();
            $("#parseResponsesSpinner").show();
        },
        // hides the spinner after completion of request, whether successfull or failor.
        complete: function() {
            $("#parseResponsesSpinner").hide();
            $("#parseResponses").show();
        },
        success: function(data) {
            $("#parseResponsesSuccess").show();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $("#parseResponsesError").show();
        },
    })
});

//Alert should be able to reappear (BS will remove it after first close)
$(function() {
   $(document).on('click', '.close', function() {
       $(this).parent().hide();
   })
});
$("#parseResponses").click(function() {
    $.ajax({
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
        type: 'GET',
    })
});

$("#writeResponses").click(function() {
    $.ajax({
        url: "/admin/api/read/",
        // shows the spinner element before sending.
        beforeSend: function() {
            $("#writeResponses").hide();
            $("#writeResponsesSpinner").show();
        },
        // hides the spinner after completion of request, whether successfull or failor.
        complete: function() {
            $("#writeResponsesSpinner").hide();
            $("#writeResponses").show();
        },
        success: function(data) {
            $("#writeResponsesSuccess").show();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $("#writeResponsesError").show();
        },
        type: 'GET',
    })
});

//Alert should be able to reappear (BS will remove it after first close)
$(function() {
   $(document).on('click', '.close', function() {
       $(this).parent().hide();
   })
});
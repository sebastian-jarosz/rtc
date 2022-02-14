// this is the id of the form
$("#generatorForm").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var actionUrl = form.attr('action');

    $.ajax({
        type: "POST",
        url: actionUrl,
        data: form.serialize(),
        beforeSend: function() {
            $("#generateTraining").hide();
            $("#generateTrainingSpinner").show();
        },
        // hides the spinner after completion of request, whether successfull or failor.
        complete: function() {
            $("#generateTrainingSpinner").hide();
            $("#generateTraining").show();
        },
        success: function(data) {
            $("#generateTrainingSuccess").show();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $("#generateTrainingError").show();
        },
    });

});

$(document).ready(function() {
    // Hide Other Trainings field (checkbox is not checked)
    // Hide whole div, but remove required from input
    $('#div_id_other_trainings_amount').hide()
    $("#id_other_trainings_amount").prop('required', false)
    // Hide whole div, but remove required from input
    $('#div_id_other_trainings_time').hide()
    $('#id_other_trainings_time').prop('required', false)


    // Hide Wellness field (checkbox is not checked)
    $('#div_id_wellness_amount').hide()
    $("#id_wellness_amount").prop('required', false)

    $('#id_other_trainings').change(function() {
        if(this.checked) {
            $('#div_id_other_trainings_amount').show()
            $("#id_other_trainings_amount").prop('required', true)
            $('#div_id_other_trainings_time').show()
            $('#id_other_trainings_time').prop('required', false)
        } else {
            $('#div_id_other_trainings_amount').hide()
            $("#id_other_trainings_amount").prop('required', false)
            $('#div_id_other_trainings_time').hide()
            $('#id_other_trainings_time').prop('required', false)
        }
    });

    $('#id_wellness').change(function() {
        if(this.checked) {
            $('#div_id_wellness_amount').show()
            $("#id_wellness_amount").prop('required', true)
        } else {
            $('#div_id_wellness_amount').hide()
            $("#id_wellness_amount").prop('required', false)
        }
    });
});
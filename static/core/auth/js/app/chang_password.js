

$("#new_password").on('keydown', function () {
    $('#confirm_password').val('').parsley().reset();
});
$("#new_password").on('keyup', function () {
    if ($("#password").val() != "") {
        $('#confirm_password').attr('data-parsley-required', 'true');
    } else {
        $('#confirm_password').removeAttr('data-parsley-required');
    }
});
$(document).on('click', '.change_pass', function () {
    $("#old_password").val('').parsley().reset();
    $("#new_password").val('').parsley().reset();
    $("#confirm_password").val('').parsley().reset();
    $('#change_pass').modal();
    $('#password_save').on('click', function (e) {
        e.preventDefault();
        var pass_form_parsley = $("#change_pass_form").parsley();
        pass_form_parsley.validate();
        if (!pass_form_parsley.isValid()) {
            return;
        }
        var $form = new FormData($('#change_pass_form')[0]);
        $.ajax({
            method: "PATCH",
            processData: false,
            contentType: false,
            cache: false,
            data: $form,
            url: '/api/change_password/',
            success: function (res) {
                $("#change_pass").modal('hide');
                notify('', 'Password changed successfully', '', 'success', 2000);
                setTimeout(function () {
                    window.location='/login/'
                    // location.reload();
                }, 2500);
            },
            error: function (res) {
                var errors = res.responseText;
                $.each(JSON.parse(errors), function (key, value) {
                    var nMessage = value;
                    notify('', nMessage, '', 'danger');
                });
            }

        })
    });
});
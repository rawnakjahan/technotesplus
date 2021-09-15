//change form upon action (add/edit)
function SetForm($modal, $form, method, update_item_id) {
    ResetForm($form);
    update_item_id = update_item_id || null;
    let modal_title = '';
    let submit_button_name = '';

    if (method === 'post') {
        modal_title = 'Add New';
        submit_button_name = 'Save'
    } else {
        modal_title = 'Update';
        submit_button_name = 'Update';
    }

    $modal.find('.modal-title span').text(modal_title);
    $form.attr('method', method);
    $form.attr('data-item_id', update_item_id);
    $form.find('button[type=submit]').text(submit_button_name);
    if (method==='post' && $form.find('button[type=submit]#save_reuse_entry_button').length ===1){
        $form.find('button[type=submit]#save_reuse_entry_button').removeClass('hidden').text("Save & reuse");
    }else{
         $form.find('button[type=submit]#save_reuse_entry_button').addClass('hidden');
    }


}

function ResetForm($form) {
    $form.trigger('reset');
    $form.find(".help-block").empty();
    $form.find('.form-group').removeClass('has-error');
    $form.find('.fg-line').removeClass('fg-toggled');
    $form.find('.selectpicker').val('');
    $form.find('.selectpicker').selectpicker('refresh');

}

function DeleteItem(delete_url, $dt_table) {
    swal({
        title: "Are you sure?",
        text: "You will not be able to recover this Information!",
        type: "warning",
        showCancelButton: true,
        confirmButtonText: "Delete",
        cancelButtonText: "Cancel",
    }).then(function (isConfirm) {
        if (isConfirm) {
            $.ajax({
                type: "DELETE",
                url: delete_url,
                processData: false,
                contentType: false,
                success: function () {
                    $dt_table.clearPipeline().draw();
                    notify('Congratulations!!! ', 'Information has been Deleted Successfully', '', 'success');
                },
                error: function (response) {
                    let errors = response.responseText;
                    if (response.status === 403 ||response.status === 400) {
                        $.each(JSON.parse(errors), function (key, value) {
                            let nMessage = key.toUpperCase() + ": " + value;
                            notify('', nMessage, '', 'danger', 10000);
                        });
                    } else {
                        notify('', 'Sorry ! You can not delete this item.', '', 'danger', 8000);
                    }
                }
            });
        } else {
            return false;
        }
    });
}

function SelectPickerLoadDataFromApi($field, api_url, value, label, selected_value, add_data_attr) {
    selected_value = selected_value || '';
    add_data_attr = add_data_attr || null;
    $field.find('option').remove();
    $field.append("<option value=''>Nothing selected</option>");
    $.ajax({
        type: "GET",
        url: api_url,
        success: function (data) {
            $.each(data, function (i, d) {
                // console.log(data);
                $field.append($('<option>', {
                    value: d[value],
                    text: d[label],
                }));
                if (add_data_attr) {
                    $.each(add_data_attr, function (name, value) {
                        $field.find('option:last').attr(name, d[value])
                    })
                }
            });
            $field.selectpicker('val', selected_value);
            $field.selectpicker('refresh')
        },
        error: function (response) {
        }
    });
}


function SelectPickerLoadDataFromApiForPendingRequisition($field, api_url, value, label, selected_value, add_data_attr) {
    selected_value = selected_value || '';
    add_data_attr = add_data_attr || null;
    $field.find('option').remove();
    $field.append("<option value=''>Nothing selected</option>");
    $.ajax({
        type: "GET",
        url: api_url,
        success: function (data) {
            $.each(data, function (i, d) {
                // console.log(data);
                $field.append($('<option>', {
                    value: d[value],
                    text: d[label] + ' (Branch: ' + d.branch + ', Requester Name: ' + d.requester_name + ', Department: ' + d.department + ' )',
                }));
                if (add_data_attr) {
                    $.each(add_data_attr, function (name, value) {
                        $field.find('option:last').attr(name, d[value])
                    })
                }
            });
            $field.selectpicker('val', selected_value);
            $field.selectpicker('refresh')
        },
        error: function (response) {
        }
    });
}

function MakeRequired(elements) {
    $.each(elements, function (i, element) {
        element.attr('data-parsley-required', 'true');
        // if (element.closest('.fg-line').find('span.required_star').length === 0) {
        //     element.closest('.fg-line').append('<span class="required_star">*</span>');
        // }
    });
}

function MakeNonRequired(elements) {
    $.each(elements, function (i, element) {
        element.removeAttr('data-parsley-required');
        // element.closest('.fg-line').find('span.required_star').remove();
        // element.closest('.fg-line').find('label.fg-label').css({'color': '', 'font-weight': '500'});
    });
}
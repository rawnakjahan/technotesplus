{
    let $table = $('#stock_list'),
        $add_stock_button = $('#add_stock_button'),
        $edit_stock_button = $('#edit_stock_button'),
        $action_buttons = $("#add_stock_button, #edit_stock_button"),
        $delete_stock_button = $('#delete_stock_button'),
        $stock_add_edit_modal = $('#stock_add_edit_modal'),
        $stock_add_edit_form = $('#stock_add_edit_form'),
        $save_stock_button = $('#save_stock_button');

    //Data table
    $table.DataTable({
        processing: true,
        serverSide: true,
        dom: 'Bfrtip',
            buttons: [
                'copy', 'csv', 'excel'
            ],
        ajax: $.fn.dataTable.pipeline({
            url: toner_stock_api,
            pages: 1 // number of pages to cache
        }),
        scrollY: 300,
        deferRender: true,
        scroller: true,
        columns: [
            {"title": "Title", "data": 'title'},
            {"title": "Content", "data": "content"},
            {"title": "Created By", "data": "created_user_name"},
        ],
        columnDefs: [
            {
                targets: 0,
                width: "25%",
            },
            {
                targets: 1,
                width: "65%"
            },{
                targets: 2,
                width: "10%"
            },
        ]
    });

    let $dt_table = $table.DataTable();
    $table.find('tbody').on('click', 'tr', function () {
        let data = $dt_table.row(this).data();

        if ($(this).hasClass('selected')) {
            $(this).removeClass('selected');
            $delete_stock_button.removeData('item-id').removeClass('c-black');
            $edit_stock_button.removeData('item-id').removeClass('c-black');
        } else {
            $dt_table.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
            $delete_stock_button.removeData("item-id").data("item-id", data.id);
            $delete_stock_button.addClass("c-black");
            $edit_stock_button.removeData("item-id").data("item-id", data.id);
            $edit_stock_button.addClass("c-black");

            $delete_stock_button.attr({
                "data-toggle": "modal",
                "data-target": ""
            });

            $edit_stock_button.attr({
                "data-toggle": "modal",
                "data-target": ""
            });

        }
    });

    //Add Modal
    $add_stock_button.on('click', function () {
        SetForm($stock_add_edit_modal, $stock_add_edit_form, 'post');
        $stock_add_edit_modal.modal().show();
    });

    //Edit Modal
    $edit_stock_button.on('click', function () {
        if ($(this).data('item-id')) {
            let update_item_id = $(this).data('item-id');

            SetForm($stock_add_edit_modal, $stock_add_edit_form, 'patch', update_item_id);

            $.ajax({
                type: "GET",
                url: toner_stock_api + update_item_id,
                success: function (data) {
                    $('#note_title').val(data.title);
                    $('#note_content').val(data.content);
                },
                error: function (response) {
                }
            });


            $stock_add_edit_modal.modal().show();
        } else {
            notify('No Stock selected!!! ', 'Please select a Stock first', '', 'danger', 5000);
        }
    });

    // Add Edit Form submit
    $save_stock_button.on('click', (e) => {
        e.preventDefault();
        let $form = $stock_add_edit_form;
        let $modal = $stock_add_edit_form.closest('.modal');
        let $method = $form.attr('method');
        let $url = toner_stock_api;
        let update_item_id = $form.attr('data-item_id');

        (($method === 'patch') && update_item_id != null) ? $url = $url + update_item_id + '/' : '';

        let process_form = $form.parsley();
        process_form.validate();

        if (process_form.isValid()) {
            $.ajax({
                url: $url,
                method: $method,
                data: $form.serialize(),
                success: () => {
                    let success_action = ($method === 'post') ? 'Added' : 'Updated';
                    notify('Congratulations!!! ', 'Information ' + success_action + ' Successfully', '', 'success', '3000');
                    $dt_table.clearPipeline().draw();
                    $form.trigger('reset');
                    $modal.modal('toggle');
                },
                error: (res) => {
                    $.each(JSON.parse(res.responseText), (k, v) => {
                        notify(`<strong>${k.substr(0, 1).toUpperCase() + k.substr(1)}:</strong> `, `<i>${v}</i>`, '', 'danger', 10000);
                    });
                }
            });
        }
    });

    //Delete
    $delete_stock_button.on('click', function () {

        let delete_item_id = $(this).data('item-id');

        if ($(this).data('item-id')) {
            let delete_item_url = toner_stock_api + delete_item_id;
            DeleteItem(delete_item_url, $dt_table);
        } else {
            notify('No Item selected!!! ', 'Please select a Item first', '', 'danger');
        }
    });


    //pagination button on click remove data-item-id from actions
    $(document).on('click', '.paginate_button', function () {
        if ($('.dataTable').find('.selected').length > 0) {
            $action_buttons.removeData('item-id').removeClass('c-black');
            $('.dataTable tbody tr').removeClass('selected');
        } else {

        }
    });


}

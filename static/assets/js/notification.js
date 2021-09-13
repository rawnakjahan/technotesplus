/**
 * Created by rawnak on 4/30/17.
 */

(function () {
    var count = 0; //count of announcements
    var task_count = 0; //count of tasks
    var total_count = 0; //total counts
    var t_loop = 0; //for top 5 comments
    var a_loop = 0;
    // if (WORKFLOW == 'aBX3RODumf') {
    //     //Count top 5 tasks and show in the list
    //     $.ajax({
    //         type: "GET",
    //         url: inbox + "?item_status=todo&id=notifier",
    //         dataType: "json",
    //         success: function (data) {
    //             $.each(data, function (i, d) {
    //                 if (t_loop != 5) {
    //                     $('#task_list').append("<a class='list-group-item media' data-task=" + d.task + " data-application=" + d.application + " href='#'>You have a task from <span style='color:#009688'><b>" + d.sent_by + "</b></span>, app: <span style='color:#009688'><b>" + d.app_number + "</b></span></a>");
    //                     t_loop++;
    //                 }
    //             });
    //             if (data.length > 5) {
    //                 $('#task_list').append("<a class='view-more f-500' style='color:#009688' href='/workflow/case/inbox/'#'>View More Task</a>")
    //             }
    //
    //             $('#task_list').find("a:not('.view-more')").on("click", function (event) {
    //                 event.preventDefault();
    //                 var outer = {
    //                     application: $(this).data('application'),
    //                     task: $(this).data('task')
    //                 };
    //
    //                 localStorage.setItem("outer", JSON.stringify(outer));
    //                 var tasks_url = "/workflow/case/inbox/";
    //                 window.location = tasks_url;
    //             });
    //         },
    //         error: function (response) {
    //             console.log(response);
    //         }
    //     });
    //
    //     //Count tasks
    //     $.ajax({
    //         type: "GET",
    //         url: inbox + "?item_status=todo&id=count",
    //         dataType: "json",
    //         success: function (data) {
    //             task_count = data.count;
    //             if (task_count === 0) {
    //                 $("#task_counts").html("No");
    //             } else {
    //                 $("#task_counts").html(task_count);
    //             }
    //             total_count = total_count + task_count;
    //             $("#count").empty().html(total_count);
    //         },
    //         error: function (response) {
    //             console.log(response);
    //         }
    //     });
    // }
    //Count unseen comments from api

    // $.ajax({
    //     type: "GET",
    //     url: all_recipients_api,
    //     dataType: "json",
    //     success: function (data) {
    //
    //         $.each(data, function (i, d) {
    //             if (d.status == "unseen" && d.users == userId) {
    //                 count++;
    //             }
    //         });
    //         if (count == 0) {
    //             $("#announce_count").html("No");
    //         } else {
    //             $("#announce_count").html(count);
    //         }
    //
    //         total_count = total_count + count;
    //
    //         $("#count").empty().html(total_count);
    //
    //
    //     },
    //     error: function (response) {
    //         console.log(response);
    //
    //     }
    // });


    var update_data = {
        status: "seen",
    };


    //ANNONCEMENT NOTIFICATIONS CLICK
    // $("#announcements").on("click", function (event) {
    //     event.preventDefault();
    //     $.ajax({
    //         type: "GET",
    //         url: all_recipients_api,
    //         dataType: "json",
    //         success: function (data) {
    //             var id_count = 0;
    //             var unseen_comments_id = []; //unseen comments ids
    //             $.each(data, function (i, d) {
    //
    //                 if (d.status == "unseen" && d.users == userId) {
    //
    //                     unseen_comments_id[id_count] = d.id;
    //                     id_count++;
    //                 }
    //             });
    //
    //             for (u = 0; u < unseen_comments_id.length; u++) {
    //                 // console.log(all_recipients_api + unseen_comments_id[u]);
    //                 var status_url = "/socket/status/" + unseen_comments_id[u] + "/";
    //                 $.ajax({
    //                     type: "PATCH",
    //                     url: status_url,
    //                     data: JSON.stringify(update_data),
    //                     "processData": false,
    //                     "headers": {
    //                         "content-type": "application/json",
    //                     },
    //                     success: function (data) {
    //                         // console.log("successful");
    //                     },
    //                     error: function (response) {
    //                         console.log(response);
    //                     }
    //
    //                 });
    //
    //             }
    //             total_count = total_count - count;
    //             count = 0;
    //             if (count == 0) {
    //                 $("#announce_count").html("No");
    //             } else {
    //                 $("#announce_count").html(count);
    //             }
    //             $("#count").empty().html(total_count);
    //             window.location = announcement_url;
    //
    //         },
    //         error: function (response) {
    //             console.log(response);
    //         }
    //     });
    //
    //
    // });

    // if (LIVE_NOTIFICATION === 'True') {
    //     //SOCKET OPERATIONS
    //     var socket = io.connect(location.protocol + '//' + location.hostname + ':' + socket_listening_port);
    //     console.log(location.protocol + '//' + location.hostname + ':' + socket_listening_port)
    //     if (DMS = "9dL53eBFDK") {
    //         socket.on('pending', function (message) {
    //             var html = '<a href="/dms/document/upload/standard_upload/filesave/pendingmetalist/" id="zmdi-cloud-done" class="c-black"><i class="zmdi zmdi-cloud-done c-black m-r-2"></i>' + " Pending Documents(" + message + ")" + '</a>';
    //             $("#zmdi-cloud-done").empty().append(html);
    //         });
    //     }
    //
    //
    //     socket.on('announcement', function (message) {
    //         var flag = 0;
    //         //Escape HTML characters
    //         var data = message.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    //
    //         //Append message to the bottom of the list
    //         //new
    //         var chat_data = JSON.parse(data);
    //         for (i = 0; i < chat_data.recipients.length; i++) {
    //
    //             if (chat_data.recipients[i] == userId) {
    //
    //
    //                 flag = 1;
    //
    //             }
    //         }
    //
    //         var elem = ($.parseHTML(chat_data.message)[0].data);
    //         if (flag == 1) {
    //
    //             count++;
    //             if (count == 0) {
    //                 $("#announce_count").html("No");
    //             } else {
    //                 $("#announce_count").html(count);
    //             }
    //             total_count++;
    //             $("#count").empty().html(total_count);
    //             $("#modal_msg").html(elem);
    //             $('#single_message').modal().show();
    //             flag = 0;
    //         }
    //
    //     });
    //     if (WORKFLOW == 'aBX3RODumf') {
    //         socket.on('task', function (message) {
    //             var flagt = 0;
    //
    //             //Escape HTML characters
    //             var data = message.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    //
    //             //Append message to the bottom of the list
    //             //new
    //             var chat_data = JSON.parse(data);
    //
    //             for (i = 0; i < chat_data.recipients.length; i++) {
    //
    //                 if (chat_data.recipients[i] == userId) {
    //
    //                     flagt = 1;
    //
    //                 }
    //             }
    //
    //             var elem = ($.parseHTML(chat_data.message)[0].data);
    //             if (flagt == 1) {
    //
    //                 task_count++;
    //                 if (task_count == 0) {
    //                     $("#task_counts").html("No");
    //                 } else {
    //                     $("#task_counts").html(task_count);
    //                 }
    //                 total_count++;
    //                 $("#count").empty().html(total_count);
    //                 $("#modal_task").html(elem);
    //                 $("#single_task").modal().show();
    //                 //here
    //                 flagt = 0;
    //
    //                 //new
    //                 $.ajax({
    //                     type: "GET",
    //                     url: inbox + "?item_status=todo",
    //                     dataType: "json",
    //                     success: function (data) {
    //                         append_count = 0;
    //                         $.each(data, function (i, d) {
    //                             if (append_count == 0) {
    //                                 $('#task_list').prepend("<a class='list-group-item media' data-task=" + d.task + " data-application=" + d.application + " href='#'>You have a task from <span style='color:#009688'><b>" + d.sent_by + "</b></span>, app:<span style='color:#009688'><b>" + d.app_number + "</b></span></a>");
    //                                 a_loop++;
    //                                 if ((t_loop + a_loop) >= 5) {
    //                                     document.getElementById("task_list").lastChild.remove();
    //                                 }
    //
    //                                 append_count++;
    //
    //                             }
    //
    //                         });
    //                         $('#task_list').find("a").on("click", function (event) {
    //                             event.preventDefault();
    //                             var outer = {
    //                                 application: $(this).data('application'),
    //                                 task: $(this).data('task')
    //                             };
    //
    //                             localStorage.setItem("outer", JSON.stringify(outer));
    //                             var tasks_url = "/workflow/case/inbox/";
    //                             window.location = tasks_url;
    //
    //                         });
    //
    //
    //                     },
    //                     error: function (response) {
    //                         console.log(response);
    //                     }
    //                 });
    //                 //new
    //             }
    //
    //
    //         });
    //     }
    //     var windowHeight = $(window).height();
    //     var newHeight = Math.round((80 / 100) * windowHeight);    //60 % OF CURRENT WINDOW HEIGHT
    //     $('#notification_bar').css({
    //         "height": newHeight, "overflow-y": "auto"
    //     });
    // }

    // get notifications
    get_latest_ten_notification = () => {
        $.ajax({
            type: "GET",
            url: get_latest_ten_notification_url,
            dataType: "json",
            success: function (data) {

                if (data.data.length === 0) {
                    // as no notification found show a generic message
                    $('#no-notification').removeClass('hidden');
                }else {
                    $.map(data.data.reverse(), function (value, index) {
                        if (value.visibility_level === 0) {
                            let url = value.redirect_url ? value.redirect_url : '#';
                            notify(
                                `<a style="color: white" href="${url}">${value.title}</a>`, '', '', 'info', 10000);
                            update_notification(value.id);
                            // $('#task_list').append("<a class='list-group-item media' data-task=" + d.task + " data-application=" + d.application + " href='#'>You have a task from <span style='color:#009688'><b>" + d.sent_by + "</b></span>, app: <span style='color:#009688'><b>" + d.app_number + "</b></span></a>");
                        }

                        // do not add same notification twice
                        if (!$('#task_list a').hasClass(`custom_${value.id}`)) {
                            let url = value.redirect_url ? value.redirect_url : '#';
                            let extra_css = (value.visibility_level < 3) ? 'h5' : '';
                            let font_color = (value.visibility_level < 3) ? '' : '#373636';
                            $('#task_list').prepend(`
                                <div class="list-group-item media" style="border-bottom: 1px solid #efe8e8;">
                                    <span style="font-size: .8em">${moment(value.created_at).format('MMMM Do YYYY, h:mm:ss a')}</span><br>
                                    <a 
                                        class='${extra_css} custom_${value.id}' 
                                        data-id=${value.id} href='${url}'
                                        style="font-size: 1em; color:${font_color}"
                                    >
                                        ${value.title}
                                    </a>
                                </div>
                            `);
                        }
                    });

                    // on click notification update each notification visibility level from notification list
                    $('#task_list .list-group-item a').on('click', function (e) {
                        let id = $(this).data('id');
                        update_notification(id, 3);
                    });
                }
            },
            error: function (response) {
                console.log(response);

            }
        });
    };

    // update visibility level of an existing notifications
    update_notification = (notification_id, visibility_level=1) => {
        $.ajax({
            type: "GET",
            url: update_notification_url + `?notification_id=${notification_id}&visibility_level=${visibility_level}`,
            dataType: "json",
            success: function (data) {
                if (visibility_level === 3) {
                    $(`.custom_${notification_id}`).removeClass('h5').css('color', '#373636');
                }
                // recount unseen notifications and update bell icon
                count_unseen_notification();
            },
            error: function (response) {
                console.log(response);

            }
        });
    };

    // get count of unseen notifications
    count_unseen_notification = () => {
        $.ajax({
            type: "GET",
            url: count_unseen_notifications_url,
            dataType: "json",
            success: function (data) {
                $("#count").empty().html(data.data);
            },
            error: function (response) {
                console.log(response);

            }
        });
    };

    // REAL TIME NOTIFICATION
    count_unseen_notification();
    get_latest_ten_notification();

    // Notifications will automatically check after every 15 sec if LIVE_NOTIFICATION is True at licensed.py
    if (LIVE_NOTIFICATION === 'True') {
        setInterval(function (e) {
            count_unseen_notification();
            get_latest_ten_notification();
        }, 15000);
    }

    // on click notification bell icon update notification visibility level
    $('#notification_bell').on('click', function (e) {
        update_notification('all_visibility_level_less_then_2', 2);
    });
})();

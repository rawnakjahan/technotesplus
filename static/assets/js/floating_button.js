class FloatingButton {
    draggable_button = $( "#draggable" );

    drag_functionality = () => {
        let self = this;
        self.draggable_button.draggable({
            axis: "x",
            containment: 'body',
            start:function(event,ui) {
                $('#draggable').css('top', '');
            },
            drag:function(event,ui) {
                $('#draggable').css('top', '');
            },
            stop:function(event,ui) {
                let position = ui.position;
                window.localStorage.setItem('floatButtonPositionX', position.left + 'px');
                window.localStorage.setItem('floatButtonPositionY', position.top + 'px');
                $('#draggable').css('top', '');
            }
        });
    };

    set_base_button_position = () => {
        if (window.localStorage.getItem('floatButtonPositionX')) {
            $('#draggable').css('left', window.localStorage.getItem('floatButtonPositionX'))
        }
        if (window.localStorage.getItem('floatButtonPositionY')) {
            $('#draggable').css('bottom', '60px');
        }
    };

    show_options = () => {
        $(document).on('mouseenter', '#draggable ul .base_button', function (e) {
            $('.option').addClass('option_new_position')
        });
        $(document).on('mouseleave', '#draggable ul', function (e) {
            $('.option').removeClass('option_new_position')
        })
    };

    main = () => {
        this.drag_functionality();
        this.set_base_button_position();
        this.show_options();
    }
}

new FloatingButton().main();

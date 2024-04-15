$(function() {

    "use strict";
    var wind = $(window);


    var wind = $(window);
        wind.on('scroll', function () {
            $(".bar span").each(function () {
                var bottom_of_object =
                $(this).offset().top + $(this).outerHeight();
                var bottom_of_window =
                $(window).scrollTop() + $(window).height();
                var myVal = $(this).attr('data-width');
                if(bottom_of_window > bottom_of_object) {
                    $(this).css({
                        width : myVal
                    });
                }
            });
        });
    });
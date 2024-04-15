
(function ($) {
  "use strict";

//scroll up start here
$(function () {
  //Check to see if the window is top if not then display button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $('.scrollToTop').css({
          'bottom': '2%',
          'opacity': '1',
          'transition': 'all .5s ease'
      });
    } else {
      $('.scrollToTop').css({
          'bottom': '-30%',
          'opacity': '0',
          'transition': 'all .5s ease'
      })
    }
  });
  //Click event to scroll to top
  $('.scrollToTop').on('click', function () {
      $('html, body').animate({
          scrollTop: 0
      }, 500);
      return false;
  });

  //preloader script here
  var img = $('.bg-img');
  img.css('background-image', function () {
      var bg = ('url(' + $(this).data('background') + ')');
      return bg;
  });
  $('.preloader').fadeOut(1000);

});


// scroll navbar
$(window).scroll(function() {
  if ($(document).scrollTop() > 150) {
      $('.header').addClass('affix');
      console.log("OK");
  } 
  else {
      $('.header').removeClass('affix');
  }
});


  // Hero Swiper
  new Swiper(".hero-slider", {
    loop: true,
    autoplay: {
      delay: 7000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      type: "fraction",
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  // Testimonial Swiper
  new Swiper(".testimonial", {
    // slidesPerView: 2,
    spaceBetween: 30,
    slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    autoplay: {
      delay: 7000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      300: {
        slidesPerView: 1,
        spaceBetween: 20,
      },
      770: {
        slidesPerView: 2,
        spaceBetween: 40,
      },
    },
  });

  
  if (document.getElementById('eventId')) {
    // Event-single Swiper
    new Swiper(".event", {
      // slidesPerView: 3,
      spaceBetween: 30,
      slidesPerGroup: 1,
      loop: true,
      loopFillGroupWithBlank: true,
      autoplay: {
        delay: 7000,
        disableOnInteraction: false,
      },
      
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints: {
        200: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 40,
        },
        1200: {
          slidesPerView: 3,
          spaceBetween: 50,
        },
      },
    });
  }

  // About Swiper
  new Swiper(".about-slider", {
    slidesPerView: 1,
    spaceBetween: 30,
    slidesPerGroup: 1,
    loop: true,
    loopFillGroupWithBlank: true,
    autoplay: {
      delay: 7000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  // About Donar
  new Swiper(".about-donar", {
    // slidesPerView: 5,
    spaceBetween: 40,
    slidesPerGroup: 1,
    loop: true,
    loopFillGroupWithBlank: true,
    autoplay: {
      delay: 7000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 4,
        spaceBetween: 40,
      },
      1024: {
        slidesPerView: 5,
        spaceBetween: 50,
      },
    },
  });


  // About Volunteers
  new Swiper(".about-volunteers", {
    // slidesPerView: 3,
    spaceBetween: 30,
    slidesPerGroup: 1,
    loop: true,
    loopFillGroupWithBlank: true,
    autoplay: {
      delay: 7000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      640: {
        slidesPerView: 1,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 40,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 50,
      },
    },
    
  });


// Counter Section
  $.fn.jQuerySimpleCounter = function( options ) {
    var settings = $.extend({
        start:  0,
        end:    100,
        easing: 'swing',
        duration: 400,
        complete: ''
    }, options );

    var thisElement = $(this);

    $({count: settings.start}).animate({count: settings.end}, {
        duration: settings.duration,
        easing: settings.easing,
        step: function() {
            var mathCount = Math.ceil(this.count);
            thisElement.text(mathCount);
        },
        complete: settings.complete
    });
};

$('#count-1').jQuerySimpleCounter({end: 200,duration: 4000});
$('#count-2').jQuerySimpleCounter({end: 65,duration: 4000});
$('#count-3').jQuerySimpleCounter({end: 100,duration: 4000});


// Progress bar
jQuery(document).ready(function(){
  
    jQuery('.progress-bar').each(function() {
      jQuery(this).find('.progress-content').animate({
        width:jQuery(this).attr('data-percentage')
      },5000);
      
      jQuery(this).find('.progress-number-mark').animate(
        {left:jQuery(this).attr('data-percentage')},
        {
         duration: 5000,
         step: function(now, fx) {
           var data = Math.round(now);
           jQuery(this).find('.percent').html(data + '%');
         }
      });  
    });
});


// Portfolio Section
$(window).on("load", function() {

  /*========Portfolio Isotope Setup========*/
  if ($(".portfolio-section").length) {
    var $elements = $(".portfolio-section");
    $elements.isotope();
    $(".port-filter ul li").on("click", function() {
      $(".port-filter ul li").removeClass("filter-item");
      $(this).addClass("filter-item");
      var selector = $(this).attr("data-filter");
      $(".portfolio-section").isotope({
        filter: selector,
        animationOptions: {
          duration: 750,
          easing: "linear",
          queue: false,
        },
      });
    });
  }
});


// MagnificPopup
$(document).ready(function(){
  $('.image-popup-vertical-fit').magnificPopup({
    type: 'image',
    mainClass: 'mfp-with-zoom', 
    gallery:{
      enabled:true
    },
  
    zoom: {
      enabled: true, 
  
      duration: 300, // duration of the effect, in milliseconds
      easing: 'ease-in-out', // CSS transition easing function
  
      opener: function(openerElement) {
        return openerElement.is('img') ? openerElement : openerElement.find('img');
      }
    }
  });
});


// init Masonry
var $grid = $('.grid').masonry({
  itemSelector: '.grid-item',
  percentPosition: true,
  columnWidth: '.grid-sizer'
});


// Accrodion tab
jQuery('document').ready(function($){
  $('.dropdown__top').click(function(){
    if ($(this).parent(".dropdown").hasClass("open")) {
      $(this).parent(".dropdown").removeClass("open");
      $(this).siblings(".dropdown__btm").slideUp(500);
    } else {
      $(".dropdown").removeClass("open");
      $(".dropdown .dropdown__btm").slideUp(500);
      $(this).parent(".dropdown").addClass("open");
      $(this).siblings(".dropdown__btm").slideDown(500);
    }
  })
});

// $(".form").parsley();


//contact form js
$(function () {
    // Get the form.
    var form = $('#contact-form');

    // Get the messages div.
    var formMessages = $('.form__message');

    // Set up an event listener for the contact form.
    $(form).submit(function (e) {
        // Stop the browser from submitting the form.
        e.preventDefault();

        // Serialize the form data.
        var formData = $(form).serialize();

        // Submit the form using AJAX.
        $.ajax({
                type: 'POST',
                url: $(form).attr('action'),
                data: formData
            })
            .done(function (response) {
                // Make sure that the formMessages div has the 'success' class.
                $(formMessages).removeClass('error');
                $(formMessages).addClass('success');

                // Set the message text.
                $(formMessages).text(response);

                // Clear the form.
                $('#contact-form input, #contact-form textarea').val('');
            })
            .fail(function (data) {
                // Make sure that the formMessages div has the 'error' class.
                $(formMessages).removeClass('success');
                $(formMessages).addClass('error');

                // Set the message text.
                if (data.responseText !== '') {
                    $(formMessages).text(data.responseText);
                } else {
                    $(formMessages).text('Oops! An error occured and your message could not be sent.');
                }
            });
    });
});


}(jQuery));




//# sourceMappingURL=script.js.map
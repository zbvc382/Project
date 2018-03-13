$(document).ready(function () {

    $(".links").each(function () {
        if ($('a', this).attr("href") === window.location.pathname) {
            $(this).removeClass('inactive').addClass('active');
        }
    });

    $( "div.notification1" ).delay( 1000 ).fadeIn( 400 ).delay(4000).fadeOut( 400 );

    $( "div.notification2" ).fadeIn( 400 ).delay(3000).fadeOut( 400 );

});
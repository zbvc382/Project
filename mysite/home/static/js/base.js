$(document).ready(function() {

  $(".links").each(function() {

    if ($('a', this).attr("href") === window.location.pathname) {
      $(this).removeClass('inactive').addClass('active');
    }
  });
});
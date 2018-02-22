$(document).ready(function () {
  $("#approved-date-text").hide();
  $("#declined-date-text").hide();

  $(".requester-comment-div").wrapAll("<fieldset />");

  $('#approve-button').click(function () {
    $("input[name=status]").val("Approved");
    var comment = $("#authoriserComment").val();
    $("#id_comment").val(comment);
  });

  $('#decline-button').click(function () {
    $("input[name=status]").val("Declined");
    var comment = $("#authoriserComment").val();
    $("#id_comment").val(comment);
  });
});
$(document).ready(function () {

    $(".requester-comment-div").wrapAll("<fieldset />");

    $('#approve-button').click(function () {
        $("input[name=status]").val("Approved");
        var comment = $("#authoriserComment").val();
        if (comment.length === 0) {
            $('#helpBlock2').remove();
            $('#char-limit-mssg').remove();
            $('#authoriserComment')
                .after('<span id="helpBlock2" class="help-block">Field required</span>');
            $('#comment-div').addClass('has-error');

        }
        if (comment.length > 250) {
            $('#char-limit-mssg').remove();
            $('#helpBlock2').remove();
            $('#authoriserComment')
                .after('<span id="helpBlock2" class="help-block">Maximum character limit exceeded (250 Max)</span>');
            $('#comment-div').addClass('has-error');
            return false;
        }

        $("#id_comment").val(comment);
    });

    $('#decline-button').click(function () {
        $("input[name=status]").val("Declined");
        var comment = $("#authoriserComment").val();

        if (comment.length === 0) {
            $('#helpBlock2').remove();
            $('#char-limit-mssg').remove();
            $('#authoriserComment')
                .after('<span id="helpBlock2" class="help-block">Field required</span>');
            $('#comment-div').addClass('has-error');
        }

        if (comment.length > 250) {
            $('#char-limit-mssg').remove();
            $('#helpBlock2').remove();
            $('#authoriserComment')
                .after('<span id="helpBlock2" class="help-block">Maximum character limit exceeded (250 Max)</span>');
            $('#comment-div').addClass('has-error');
            return false;
        }
        $("#id_comment").val(comment);
    });
});
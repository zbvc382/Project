$(document).ready(function () {
    $(function () {
        $('#id_start').datetimepicker({
            format: 'DD/MM/YYYY'
        });
        $('#id_end').datetimepicker({
            format: 'DD/MM/YYYY'
        });
        $('#control-leave-attachment').addClass('has-error');


        $("#cal-button").click(function(){

            $("#drop-down").slideToggle();
        });
    });
});
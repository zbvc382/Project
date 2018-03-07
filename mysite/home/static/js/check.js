$(document).ready(function() {
    
    $('#save-button').click(function () {
        var template_name = $('#temp-name').val();
        $('#save-template-link').attr('href',function() {
            this.href = this.href.replace('template_name', template_name);
        });
        alert($('#save-template-link').attr('href'));
    })
});





// $('#save-template-link').attr('href').replace('\'name\'', template_name);
//'href', '{% url \'home:create\' request.pk \'' + template_name + '\' %}'
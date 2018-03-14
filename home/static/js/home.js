$(document).ready(function () {

    var auth_table = $('#authoriser_table').DataTable({
        "lengthMenu": [
            [8],
            [8]
        ]
    });

    var req_table = $('#requester_table').DataTable({
        "lengthMenu": [
            [5],
            [5]
        ]
    });

    // Search box
    $('#searchbox').on('keyup click', function () {
        $('.table').DataTable().search($('#searchbox').val()).draw();
    });

    $('#button-all:input').on('change', function () {
        auth_table.search('').columns().search().draw();
        auth_table.order([1, "desc"]).draw();

        req_table.search('').columns().search().draw();
        req_table.order([1, "desc"]).draw();
    });
    $('#button-pending:input').on('change', function () {
        auth_table.search(this.value).columns(6).search().draw();
        auth_table.order([1, "asc"]).draw();

        req_table.search(this.value).columns(7).search().draw();
        req_table.order([1, "desc"]).draw();
    });
    $('#button-approved:input').on('change', function () {
        auth_table.search(this.value).columns(6).search().draw();
        auth_table.order([1, "desc"]).draw();

        req_table.search(this.value).columns(7).search().draw();
        req_table.order([1, "desc"]).draw();
    });
    $('#button-declined:input').on('change', function () {
        auth_table.search(this.value).columns(6).search().draw();
        auth_table.order([1, "desc"]).draw();

        req_table.search(this.value).columns(7).search().draw();
        req_table.order([1, "desc"]).draw();
    });

    // Sets default table results to pending
    $('input[type=radio]').each(function () {
        if ($(this).is(':checked')) {
            auth_table.search(this.value).columns(5).search().draw();

            req_table.search(this.value).columns(7).search().draw();
            req_table.order([1, "desc"]).draw();
        }
    });

    $("#authoriser_table_paginate").detach().appendTo('#footer-paginate');
    $("#authoriser_table_info").detach().appendTo('#footer-info');

    $("#requester_table_paginate").detach().appendTo('#footer-paginate');
    $("#requester_table_info").detach().appendTo('#footer-info');

    // Gets the value of view-reason and appends it to modal-body
    $('.view-reason').click(function () {
        var reason = $(this).val();
        $('.modal-body').append('<p>' + reason + '</p>');
    });

    // Empties modal-body text once modal is closed
    $('#myModal').on('hidden.bs.modal', function (e) {
        $('.modal-body').empty();
    });

    // Allows list elements to be draggable
    $("#sortable").sortable();
    $("#sortable").disableSelection();

    $('[data-toggle="tooltip"]').tooltip();
});
$(document).ready(function () {
    $('#my_table').DataTable({
      "lengthMenu": [
        [25],
        [25]
      ]
    });
    // Search box
    $('#searchbox').on('keyup click', function () {
      $('.table').DataTable().search($('#searchbox').val()).draw();
    });
    var table = $('#my_table').DataTable();
    $('#button-all:input').on('change', function () {
      table.search('').columns().search().draw();
      table.order([1, "desc"]).draw();
    });
    $('#button-pending:input').on('change', function () {
      table.search(this.value).columns(6).search().draw();
      table.order([1, "asc"]).draw();
    });
    $('#button-approved:input').on('change', function () {
      table.search(this.value).columns(6).search().draw();
      table.order([1, "desc"]).draw();
    });
    $('#button-declined:input').on('change', function () {
      table.search(this.value).columns(6).search().draw();
      table.order([1, "desc"]).draw();
    });
    // Default table results (pending)
    $('input[type=radio]').each(function () {
      if ($(this).is(':checked')) {
        table.search(this.value).columns(5).search().draw();
      }
    });
    $("#my_table_paginate").detach();
    $("#my_table_info").detach();
  }

);
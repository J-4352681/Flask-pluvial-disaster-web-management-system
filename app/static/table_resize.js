$(document).ready(function() {
  var cols_per_row = $('table').children('tbody, thead').children('tr').children().length
  / $('table').children('tbody, thead').children('tr').length;
    
  $('table').children('tbody, thead').children('tr').children().each(function(index, element) {
    if(index % cols_per_row != 0
    && index % cols_per_row != cols_per_row-1
    && $(window).width() < 1000) element.style.display = 'none';
  });

  $(window).on('resize', function(){
    if ($(window).width() < 1000){
      $('table').children('tbody, thead').children('tr').children().each(function(index, element) {
        if(index % cols_per_row != 0
        && index % cols_per_row != cols_per_row-1) element.style.display = 'none';
      });
    } else {
      $('table').children('tbody, thead').children('tr').children().each(function(index, element) {
        if(index % cols_per_row != 0
        && index % cols_per_row != cols_per_row-1) element.style.display = 'block';
      });
    }
  });
});
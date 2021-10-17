$(document).ready(function(){
  $('select[multiple]').each(function(index, elem){
    mult_select = $(this);
    mult_select.hide();
    id_mult_selec = mult_select.id;
    mult_select.parent().parent().children('.help').hide();
    entity = mult_select.parent().parent().children('label').text();
    
    new_mult_select = $('<div style="display: inline-block; width: 300px;">');
    mult_select.before(new_mult_select);
    if (elem.options.length > 0){
      [...elem.options].forEach(element => {
  
        checkbox = $("<input type='checkbox' style='margin-right: 10px;'>").attr('checked', element.selected);
        label = $("<label></label>");
        new_mult_select.prepend(label.append(element.text).prepend(checkbox));

        console.log(checkbox, element.value, $(this));
  
        checkbox.click(function(){ element.selected = !element.selected; });
      });
    } else {
      label = $("<label></label>");
      new_mult_select.prepend(label.append('Sin ' + entity + ' para seleccionar'));
    }
  });
});
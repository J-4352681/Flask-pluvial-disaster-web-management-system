$(document).ready(function() {
  let menu = $('#nav-drop-menu'), menu_width =  menu.outerWidth(true);
  let u_icon = $('#nav-user-icon'), u_icon_width = u_icon.outerWidth(true), u_icon_height = u_icon.outerHeight(true), u_icon_pos = u_icon.position();
  let navbar = $('#navbar'), nv_height = navbar.outerHeight(true);
  
  menu.css('left', u_icon_pos.left - menu_width + u_icon_width/2 + 'px');
  menu.css('top', u_icon_pos.top + nv_height + 'px');
  
  u_icon.click(function() {
    if(menu.css('visibility') == 'hidden') menu.css('visibility', 'visible');
    else menu.css('visibility', 'hidden');
  });
  
  nv_height_inc = nv_height + 50;
  
  $('.mt-navbar')
  .css('margin-top', nv_height_inc + 'px');
});
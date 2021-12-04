$( document ).ready(function() {
  var row = $('#Coordenadas');
  var row_text = row.children().last().text();
  row.hide();
  var table = $('table');
  var map_div = $('<div class="row my-3"><div id="leaflet_map" class="col" style="height: 500px;"></div></div>');
  table[0].parentNode.insertBefore(map_div[0], table[0].nextSibling);

  map = leaflet_init();
  
  L.polyline(JSON.parse(row_text.replaceAll("'", '"')), {color: '#000000'}).addTo(map);
});
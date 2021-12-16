function create_polygon(map, coord, color) {
  coord = JSON.parse(coord.replaceAll("'", '"'));
  
  if(coord.length == 1) {
    coord = coord[0];
    coord = [coord.lat, coord.lng];
    var polygon = L.marker(coord)
    .addTo(map)
  } else {
    var polygon = L.polygon(coord, {color: color})
    .addTo(map)
    .setStyle({fillOpacity: 0.5});
  }

  return polygon;
}

$( document ).ready(function() {
  var row = $('#Coordenadas').hide();
  var table = $('table');
  var map_div = $('<div class="row my-3"><div id="leaflet_map" class="col" style="height: 500px;"></div></div>');
  table[0].parentNode.insertBefore(map_div[0], table[0].nextSibling);

  map = leaflet_init();
  geoman_zone_init(map, false);
  
  polygon = create_polygon(map, row.children().last().text(), $('#Color > td:last').text());
});
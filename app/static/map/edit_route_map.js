$(document).ready(function() {
  var json_input = $('input[name="coordinates"]');
  // json_input.hide();
  json_input.parent().css({'height': '500px'});
  json_input.parent().append('<div id="leaflet_map" class="col" style="height: 500px;"></div>');

  map = leaflet_init(); // inicializo leaflet y genera el mapa
  control = routingmachine_init(map, true);

  if(json_input.val() != '') control.setWaypoints(JSON.parse(json_input.val().replaceAll("'", '"')));

  control.on('routeselected', function(e) {
    var route = e.route;
    // json_input.val(JSON.stringify(route.coordinates)); // inicializo el input que se guarda en bd
    json_input.val(JSON.stringify(control.getWaypoints().map(point => point.latLng))); // inicializo el input que se guarda en bd
  });
});
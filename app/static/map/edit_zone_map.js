function create_polygon(map, input, areaColor) {
    var polygon;
    if (input.val() != '') polygon = L.polygon(JSON.parse(input.val().replaceAll("'", '"')), {color: areaColor});
    else polygon = L.polygon([ // creo el poligono inicial (no se pude borrar, solo se puede modificar)
        [-34.92084502261776, -57.95590210065711],
        [-34.9278823538, -57.95916366681924],
        [-34.92957122347638, -57.94010925397744],
    ], {color: areaColor});

    polygon
    .addTo(map) // agrego el poligono al mapa
    .on('pm:edit', (e) => { // agrego evento al poligono para que actualice el input JSON
        input.val(JSON.stringify(polygon.getLatLngs()[0]));
    })
    .setStyle({fillOpacity: 0.5});

    return polygon;
}

$(document).ready(function() {
    var color_input; color_input_exists = false;
    if($('#color').length > 0) {
        color_input = $('#color') [0];
        color_input_exists = true;
    } else {
        color_input = {
            value: '#000000',
            val: function() {return '#000000';}
        };
    }
    if($('#code').val() == '') color_input.value = '#000000'.replaceAll('0', function(){return Math.floor(Math.random()*16).toString(16)});

    var json_input = $('input[name="coordinates"]').hide();
    json_input.parent().css({'height': '500px'});
    json_input.parent().append('<div id="leaflet_map" class="col" style="height: 500px;"></div>');

    map = leaflet_init(); // inicializo leaflet y genera el mapa 
    geoman_zone_init(map, true); // inicializo geoman (plugin para manipular leaflet mas facil)
    
    polygon = create_polygon(map, json_input, color_input.value); // creo el poligono

    if (color_input_exists){
        color_input.addEventListener('change', function(){
            // areaColor = color_input.value
            polygon.setStyle({color: color_input.value});
        });
    }

    json_input.val(JSON.stringify(polygon.getLatLngs()[0])); // inicializo el input que se guarda en bd
});
function leaflet_init() {
    var map = L.map('map').setView([-34.921408, -57.954941], 13)

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',  {
        maxZoom: 18,
        minZoom: 13,
    }).addTo(map);

    return map;
}

function geoman_init(map) {
    L.marker([51.50915, -0.096112], { pmIgnore: true }).addTo(map);

    map.pm.setLang('es');

    map.pm.addControls({  
        position: 'topleft',  
        drawCircle: false,
        drawCircleMarker: false,
        drawRectangle: false,
        drawPolyline: false,
        drawMarker: false,
        drawPolygon: false,
        cutPolygon: false,
        removalMode: false,
    });
}

function create_polygon(map, input, areaColor) {
    var polygon = L.polygon([ // creo el poligono inicial (no se pude borrar, solo se puede modificar)
        [-34.92084502261776, -57.95590210065711],
        [-34.9278823538, -57.95916366681924],
        [-34.92957122347638, -57.94010925397744],
    ], {color: areaColor})
    .addTo(map) // agrego el poligono al mapa
    .on('pm:edit', (e) => { // agrego evento al poligono para que actualice el input JSON
        input.val(JSON.stringify(polygon.getLatLngs()[0]));
    })
    .setStyle({fillOpacity: 0.5});

    return polygon;
}

$( document ).ready(function() {
    var areaColor = '#af0077';
    var color_input = $('#color')[0];
    color_input.value = areaColor;

    var json_input = $('input[name="coordinates"').hide();
    json_input.parent().css({'height': '500px'});
    json_input.parent().append('<div id="map" class="col" style="height=500px;"></div>');

    map = leaflet_init(); // inicializo leaflet y me genera el mapa 
    geoman_init(map); // inicializo geoman (plugin para manipular leaflet mas facil)
    
    polygon = create_polygon(map, json_input, areaColor); // creo el poligono

    color_input.addEventListener('change', function(){
        areaColor = color_input.value
        polygon.setStyle({color: areaColor});
    });

    json_input.val(JSON.stringify(polygon.getLatLngs()[0])); // inicializo el input que se guarda en bd
});
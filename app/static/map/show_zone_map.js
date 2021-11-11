function create_polygon(map, coord, color) {
    var polygon = L.polygon(JSON.parse(coord.replaceAll("'", '"')), {color: color})
    .addTo(map)
    .setStyle({fillOpacity: 0.5});

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
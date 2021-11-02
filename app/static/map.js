var areaColor = '#af0077';

var map = L.map('map').setView([-34.921408, -57.954941], 13)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',  {
    maxZoom: 18,
    minZoom: 13,
}).addTo(map);

var pol = L.polygon([
    [-34.92084502261776, -57.95590210065711],
    [-34.9278823538, -57.95916366681924],
    [-34.92957122347638, -57.94010925397744],
], {color: areaColor}).addTo(map);

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

map.pm.setPathOptions(
    {color: areaColor}
);
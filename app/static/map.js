var map = L.map('map').setView([-34.921408, -57.954941], 13)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',  {
    maxZoom: 18,
}).addTo(map);

var areaColor = '#000000';

var pol = L.polygon([
    [-34.92084502261776, -57.95590210065711],
    [-34.9278823538, -57.95916366681924],
    [-34.92957122347638, -57.94010925397744],
], {color: areaColor}).addTo(map);

function onMapClick(e) {
    // console.log(e.latlng);
    var point = L.point(e.latlng['lat'], e.latlng['lng']);
    var closestPoint = pol.closestLayerPoint(point);
    console.log(closestPoint['distance']);
    if (closestPoint['distance'] < 500) {
        console.log('si');
    }
    // console.log(e.latlng)
    // polygon.addLatLng(e.latlng)
}

map.on('click', onMapClick);
function leaflet_init() {
    var map = L.map('leaflet_map').setView([-34.921408, -57.954941], 13)

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',  {
        maxZoom: 18,
        minZoom: 13,
    }).addTo(map);

    return map;
}
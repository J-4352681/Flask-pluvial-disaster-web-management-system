function geoman_zone_init(map, editable) {
  L.marker([51.50915, -0.096112], { pmIgnore: true }).addTo(map);

  map.pm.setLang('es');

  if (editable) {
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
  } else {
    map.pm.disableGlobalEditMode();
  }
}
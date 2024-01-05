function routingmachine_init(map, editable) {
  var control = L.Routing.control({
    waypoints: [
        L.latLng(-34.92084502261776, -57.95590210065711),
        L.latLng(-34.92957122347638, -57.94010925397744)
    ],
    show: false,
    collapsible: false,
    addWaypoints: editable,
    draggableWaypoints: editable,
  }).addTo(map);

  return control;
}
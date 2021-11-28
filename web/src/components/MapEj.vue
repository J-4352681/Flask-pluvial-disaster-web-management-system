<template>
      <div>
          <l-map style="height: 800px" :zoom="zoom" :center="center" @click="onClick">
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-polygon :lat-lngs="polygon.latlngs" :color="polygon.color" :fill="polygon.fill" :fillColor="polygon.fillColor"></l-polygon>
            <l-marker :lat-lng="markerLatLng"></l-marker>
          </l-map>
      </div>
</template>

<script>
import {LMap, LTileLayer, LMarker, LPolygon} from '@vue-leaflet/vue-leaflet';

export default {
  name: 'MapEj',
  components: { // Componentes en: https://vue2-leaflet.netlify.app/components/
    LMap,
    LTileLayer,
    LMarker,
    LPolygon
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [-34.92149, -57.954597],
      markerLatLng: [],
      polygon: {
        latlngs: [[-34.91591853170241, -57.95511211366526], [-34.9278823538, -57.95916366681924], [-34.92957122347638, -57.94010925397744]],
        color: 'green',
        opacity: 0.5,
        fill: true,
        fillColor: 'green'
      },
    };
  },
  methods: {
    onClick(e) {
      if (e.latlng) {
        this.markerLatLng = e.latlng;
      }
      console.log(e)
    }
  }
}
</script>
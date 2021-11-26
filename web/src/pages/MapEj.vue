<template>
  <div>
    <l-map style="height: 700px" :zoom="zoom" :center="center" @click="onClick">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-marker :lat-lng="markerLatLng"></l-marker>
    </l-map>
  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker} from '@vue-leaflet/vue-leaflet';

export default {
  components: { // Componentes en: https://vue2-leaflet.netlify.app/components/
    LMap,
    LTileLayer,
    LMarker
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [-34.92149, -57.954597],
      markerLatLng: [],
      name
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
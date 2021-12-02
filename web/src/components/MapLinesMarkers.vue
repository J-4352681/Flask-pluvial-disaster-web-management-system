<template>
  <div>
    <div>
    <l-map style="height: 600px" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <div v-for="line in lines" :key="line.id">
        <l-polyline :lat-lngs="line.coordenadas" :color="line.color"></l-polyline>
      </div>
      <div v-for="marker in markers" :key="marker.id">
        <l-marker :lat-lng="marker" ></l-marker>
      </div>
    </l-map>
    </div>
  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker, LPolyline} from '@vue-leaflet/vue-leaflet';

export default {
  components: { // Componentes en: https://vue2-leaflet.netlify.app/components/
    LMap,
    LTileLayer,
    LPolyline,
    LMarker
  },
  name: 'MapLinesMarkers',
  props: { 
    lines: [],
    markers: []
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [-34.92149, -57.954597],
    };
  },
}
</script>


<style>

</style>
<template>
  <div>
    <div>
    <l-map style="height: 50vh" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <div v-for="line in lines" :key="line.id">
        <l-polyline :lat-lngs="line.puntos_ruta" :color="randomColor()" :weight="7"></l-polyline>
      </div>
      <div v-for="marker in markers" :key="marker.id">
        <l-marker :lat-lng="marker.coordenadas" >
          <l-popup>{{marker.nombre}}</l-popup>
        </l-marker>
      </div>
    </l-map>
    </div>
  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker, LPolyline, LPopup} from '@vue-leaflet/vue-leaflet';

export default {
  components: { // Componentes en: https://vue2-leaflet.netlify.app/components/
    LMap,
    LTileLayer,
    LPolyline,
    LMarker,
    LPopup
  },
  name: 'MapLinesMarkers',
  props: { 
    lines: {},
    markers: {}
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [-34.92149, -57.954597],
      randomColor: function() {return '#000000'.replaceAll('0', function(){return Math.floor(Math.random()*16).toString(16)});}
    };
  },
}
</script>


<style>

</style>
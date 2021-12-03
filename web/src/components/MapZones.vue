<template>
  <div>
    <div>
    <l-map style="height: 600px" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <div v-for="zone in zones" :key="zone.id">
        <l-polygon :lat-lngs="[zone.coordenadas]" :color="zone.color" :fill="true" :fillColor="zone.color"></l-polygon>
      </div>
    </l-map>
    </div>
  </div>
</template>

<script>
import {LMap, LTileLayer, LPolygon} from '@vue-leaflet/vue-leaflet';
import LRoutingMachine from './components/LRoutingMachine'

export default {
  components: { // Componentes en: https://vue2-leaflet.netlify.app/components/
    LMap,
    LTileLayer,
    LPolygon
  },
  name: 'MapZones',
  props: { 
    zones: {}
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
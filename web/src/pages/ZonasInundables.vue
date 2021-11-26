<template>
  <div>
    <div>
        <p>Zonas Inundables</p>
        <router-link :to="{ name: 'ZonaInundable', params: { id: '4' }}" > Ir a la zona de id 4</router-link>
    </div>
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

export default {
  components: { // Componentes en: https://vue2-leaflet.netlify.app/components/
    LMap,
    LTileLayer,
    LPolygon
  },
  name: 'ZonasInundables',
  title: 'Zonas Inundables',
  props: {},
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [-34.92149, -57.954597],
      
      zones: [],
    };
  },
  created() {
    fetch('http://localhost:5000/api/zonas_inundables/?page=1').then((response) => { //CAMBIAR por una api que devuelva todos los elementos
      console.log('primeros');
      console.log(response);
      return response.json();
    }).then((json) => {
      console.log(json);
      this.zones = json.zonas;
      console.log(this.zones);
    }).catch((e) => {
      console.log('problema');
      console.log(e)
    })
  }
}
</script>


<style>

</style>
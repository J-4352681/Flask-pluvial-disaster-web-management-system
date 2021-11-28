<template>
  <div>
    <div>
        <p>Zonas Inundables</p>
        <router-link :to="{ name: 'ZonaInundable', params: { id: '4' }}" > Ir a la zona de id 4</router-link>
    </div>
    <div>
        <MapZones :zones="fetched_zones"/>
    </div>
  </div>
</template>

<script>
import MapZones from '../components/MapZones.vue'

export default {
  name: 'ZonasInundables',
  title: 'Zonas Inundables',
  components: {
      MapZones
  },
  props: {},
  data () {
    return {
        fetched_zones: []
    };
  },
  created() {
    fetch('http://localhost:5000/api/zonas_inundables/?page=1').then((response) => { //CAMBIAR por una api que devuelva todos los elementos
      console.log('primeros');
      console.log(response);
      return response.json();
    }).then((json) => {
      console.log(json);
      this.fetched_zones = json.zonas;
      console.log(this.fetched_zones);
    }).catch((e) => {
      console.log('problema');
      console.log(e)
    })
  }
}
</script>


<style>

</style>
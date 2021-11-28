<template>
  <div>
    <div>
        <h3>Zonas Inundables</h3>
        <list :headers="shownHeaders" :items="fetched_zones"/>
    </div>
    <div>
        <MapZones :zones="fetched_zones"/>
    </div>
  </div>
</template>

<script>
import MapZones from '../components/MapZones.vue'
import list from '../components/List.vue'

export default {
  name: 'ZonasInundables',
  title: 'Zonas Inundables',
  components: {
      MapZones,
      list
  },
  props: {},
  data () {
    return {
        fetched_zones: [],
        shownHeaders: ['color', 'nombre', 'Acciones']
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
.zona{

}
</style>
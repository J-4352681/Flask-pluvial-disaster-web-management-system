<template>
  <div>
    <div>
      <p>Zona Inundable de id {{$route.params.id}}</p>
    </div>
    <div>
      <MapZones :zones="fetched_zones"/>
    </div>
  </div>
</template>

<script>
import MapZones from '../components/MapZones.vue'

export default {
  name: 'ZonaInundable',
  title () {
    return `Zonas Inundables > ${this.$route.params.id}`
  },
  components: {
      MapZones
  },
  props: {

  },
  data () {
    return {
        fetched_zones: []
    };
  },
  created() {
    var url = 'http://localhost:5000/api/zonas_inundables/' + this.$route.params.id
    fetch(url).then((response) => { //CAMBIAR por una api que devuelva todos los elementos
      console.log('primeros');
      console.log(response);
      return response.json();
    }).then((json) => {
      console.log(json);
      this.fetched_zones.push(json.atributos);
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
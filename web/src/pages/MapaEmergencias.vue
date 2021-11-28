<template>
    <div>
        <p>Mapa para Emergencias</p>
        <MapLinesMarkers :lines="fetched_lines" :markers="fetched_points" />
    </div>
</template>

<script>
import MapLinesMarkers from '../components/MapLinesMarkers.vue'

export default {
  name: 'MapaEmergencias',
  title: 'Mapa para Emergencias',
  components: {
      MapLinesMarkers
  },
  props: {},
  data () {
    return {
        fetched_lines: [],
        fetched_points: [[-34.92149, -57.954597], [-34.92109, -57.954547], [-34.92149, -57.954597], [-34.92149, -57.954597]] //Buscar con API cuando exista
    };
  },
  created() {
    fetch('http://localhost:5000/api/zonas_inundables/?page=1').then((response) => { //CAMBIAR por una api que devuelva rutas de evacuacion
      console.log('primeros');
      console.log(response);
      return response.json();
    }).then((json) => {
      console.log(json);
      this.fetched_lines = json.zonas;
      console.log(this.fetched_lines);
    }).catch((e) => {
      console.log('problema');
      console.log(e)
    });
    //AGREGAR Api que buscque puntos de encuetro
  }
}
</script>


<style>

</style>
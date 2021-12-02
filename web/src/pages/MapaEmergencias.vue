<template>
  <pageTitle title='Sección de mapa de emergencias' subtitle='En esta sección podrá visualizar el mapa con las acciones de emergencia'/>
  <section class="container">
    <MapLinesMarkers :lines="fetched_lines" :markers="fetched_points" />
  </section>
</template>

<script>
import MapLinesMarkers from '../components/MapLinesMarkers.vue'
import pageTitle from '../components/PageTitle.vue'

export default {
  name: 'MapaEmergencias',
  title: 'Mapa para Emergencias',
  components: {
      MapLinesMarkers,
      pageTitle
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
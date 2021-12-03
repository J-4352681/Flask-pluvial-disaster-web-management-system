<template>
    <div>
      <PageTitle title='Mapa para emergencias' subtitle='En esta sección podrá visualizar las rutas de evacuacion y puntos de encuentro'/>
      <section class="container">
        <div>
          <MapLinesMarkers :lines="fetched_lines" :markers="fetched_points" />
        </div>
      </section>
      <PageTitle title='Listados' subtitle='Listado de puntos de encuentro'/>
      <section class="container">
        <div>
          <List :headers="shownHeadersPoints" :items="fetched_points"/>
        </div>
      </section>
      <PageTitle subtitle='Listado de rutas de evacuacion'/>
      <section class="container">
        <div>
          <List :headers="shownHeadersLines" :items="fetched_lines"/>
        </div>
      </section>
    </div>
</template>

<script>
import MapLinesMarkers from '../components/MapLinesMarkers.vue'
import List from '../components/List.vue'
import PageTitle from '../components/PageTitle.vue'

export default {
  name: 'MapaEmergencias',
  title: 'Mapa para Emergencias',
  components: {
      MapLinesMarkers,
      List,
      PageTitle
  },
  props: {},
  data () {
    return {
        fetched_lines: [],
        fetched_points: [], //Buscar con API cuando exista. Ejemplos: [-34.92149, -57.954597], [-34.92109, -57.954547], [-34.92149, -57.954597], [-34.92149, -57.954597]
        shownHeadersPoints: ['nombre', 'direccion', 'telefono', 'email'],
        shownHeadersLines: ['nombre', 'descripcion']
    };
  },
  created() {
    //Rutas de evacuacion
    fetch('https://127.0.0.1:5000/api/recorridos-evacuacion/all').then((response) => { 
      console.log('primeros');
      console.log(response);
      return response.json();
    }).then((json) => {
      console.log(json);
      this.fetched_lines = json.routes;
      console.log(this.fetched_lines);
    }).catch((e) => {
      console.log('problema');
      console.log(e)
    });
    //Puntos de encuentro
    fetch('https://127.0.0.1:5000/api/puntos-encuentro/all').then((response) => { 
      console.log('primeros');
      console.log(response);
      return response.json();
    }).then((json) => {
      console.log(json);
      this.fetched_points = json.points;
      console.log(this.fetched_points);
    }).catch((e) => {
      console.log('problema');
      console.log(e)
    });
  }
}
</script>


<style>

</style>
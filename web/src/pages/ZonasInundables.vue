<template>
  <pageTitle title='Sección de zonas inundables' subtitle='En esta sección podrá visualizar las zonas inundables de la ciudad'/>
  <section class="container">
    <list :headers="shownHeaders" :items="fetched_zones"/>
    <MapZones :zones="fetched_zones"/>
  </section>
</template>

<script>
import MapZones from '../components/MapZones.vue'
import list from '../components/List.vue'
import pageTitle from '../components/PageTitle.vue'

export default {
  name: 'ZonasInundables',
  title: 'Zonas Inundables',
  components: {
      MapZones,
      list,
      pageTitle
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
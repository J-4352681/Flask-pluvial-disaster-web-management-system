<template>
  <div>
    <PageTitle title='Sección de zonas inundables' subtitle='En esta sección podrá visualizar las zonas inundables de la ciudad'/>
    <section class="container">
      <div>
          <MapZones :zones="fetched_zones"/>
      </div>
      <div>
          <List :headers="shownHeaders" :items="fetched_zones"/>
      </div>
    </section>
  </div>
</template>

<script>
import MapZones from '../components/MapZones.vue'
import List from '../components/List.vue'
import PageTitle from '../components/PageTitle.vue'

export default {
  name: 'ZonasInundables',
  title: 'Zonas Inundables',
  components: {
      MapZones,
      List,
      PageTitle
  },
  props: {},
  data () {
    return {
        fetched_zones: [],
        shownHeaders: ['id', 'nombre', 'color']
    };
  },
  created() {
    fetch('http://localhost:5000/api/zonas_inundables/all').then((response) => { //API que devuelve todas las zonas inundables
      console.log('primeros');
      console.log(response);
      return response.json();
    }).then((json) => {
      console.log(json);
      this.fetched_zones = json.zones;
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
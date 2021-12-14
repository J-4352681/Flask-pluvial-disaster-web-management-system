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
    fetch(process.env.VUE_APP_FLOOD_ZONES_URL)
    .then((response) => response.json())
    .then((json) => this.fetched_zones = json.zones)
    .catch((e) => console.log(e));
  }
}
</script>


<style>
</style>
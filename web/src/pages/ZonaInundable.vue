<template>
  <div>
    <PageTitle title='Zona inundable en detalle' subtitle='En esta sección podrá visualizar en detalle una zona inundable'/>
    <section class="container">
    <div>
      <MapZones :zones="fetched_zone"/>
    </div>
    <div>
      <Details :headers="shownHeaders" :items="fetched_zone"/>
    </div>
    </section>
  </div>
</template>

<script>
import MapZones from '../components/MapZones.vue'
import Details from '../components/Details.vue'
import PageTitle from '../components/PageTitle.vue'

export default {
  name: 'ZonaInundable',
  title () {
    return `Zonas Inundables > ${this.$route.params.id}`
  },
  components: {
      MapZones,
      Details,
      PageTitle
  },
  props: {

  },
  data () {
    return {
        fetched_zone: [],
        shownHeaders: ['id', 'nombre', 'color', 'coordenadas']
    };
  },
  created() {
    var url = process.env.VUE_APP_FLOOD_ZONE_SINGLE_URL + this.$route.params.id
    fetch(url).then((response) => response.json())
    .then((json) => this.fetched_zone.push(json.atributos))
    .catch((e) => console.log(e));
  }
}
</script>


<style>

</style>
<template>
    <pageTitle title='Página principal' subtitle='Bienvenido!'/>
    <mosaic title='En la app podrá realizar las siguientes acciones' :elements="mosaicElements"/>
</template>

<script>
import pageTitle from '../components/PageTitle.vue'
import mosaic from '../components/Mosaic.vue'

export default {
  name: 'Home',
  title: 'Inicio',
  props: {

  },
  components: {
      pageTitle,
      mosaic
  },
  data() {
    return {
      mosaicElements: [
        {
          title: 'Visualizar zonas inundables de la ciudad',
          description: 'Puede ver en un mapa dónde se\
          encuentran las diferentes zonas inundables\
          de la ciudad de manera gráfica e intuitiva.',
          linkName: '/zonas-inundables'
        },
        {
          title: 'Realizar denuncias',
          description: 'Puede realizar una denuncia en\
          caso de que presencie o conozca alguna\
          situación que deba ser tenida en cuenta.',
          linkName: '/denuncias'
        },
        {
          title: 'Ver mapa de denuncias',
          description: 'Puede visualizar el mapa donde\
          se encuentran ubicadas las denuncias realizadas.',
          linkName: '/mapa-denuncias'
        },
        {
          title: 'Ver el mapa de emergencias',
          description: 'Puede ver el mapa con información\
          sobre cómo actuar en situaciones de emergencia.',
          linkName: '/mapa-emergencias'
        },
        {
          title: 'Ver estadísticas',
          description: 'Puede ver las estadísticas\
          en base a la informacióno de los demás apartados.',
          linkName: '/estadisticas'
        }
      ]
    }
  }
}
</script>


<style>

</style>
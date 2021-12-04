<template>
    <pageTitle title='Página principal' subtitle='Bienvenido!'/>
    <section class="container text-justify">
      <p class="m-2">
        En este portal encontrará un protocolo de acción e información 
        relevante referente a las situaciones de inundación o precipitaciones 
        de riesgo en la cuidad de La Plata y zonas aledañas. Entre ellas se 
        encuentran las listadas a continuación.
      </p>
    </section>
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
          title: 'Visualizar los puntos de encuentro y \
          recorridos de evacuación cercanos',
          description: 'Puede ver en un mapa dónde se\
          encuentran los diferentes puntos de encuentro\
          y los recorridos de evacuación.',
          linkName: '/mapa-emergencias'
        },
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
        }
      ]
    }
  }
}
</script>


<style>
  .text-justify {text-align: justify;}

  @media (max-width: 768px) {
    .m-2 {
      margin: 10% 2%;
    }
  }

  @media (min-width: 768px) {
    .m-2 {
      margin: 35px 2% 35px 2%;
    }
  }
</style>
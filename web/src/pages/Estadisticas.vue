<template>
<div>
    <div>
    <PageTitle title='Estadisticas' subtitle='Estadisticas recolectadas por nuestra aplicacion'/>
    </div>
    <DoughnutChart> </DoughnutChart>
</div>
</template>

<script>
import DoughnutChart from '../components/DoughnutChart'
import PageTitle from '../components/PageTitle.vue'


export default {
  name: 'Estadisticas',
  components: { DoughnutChart, PageTitle },
};
</script>
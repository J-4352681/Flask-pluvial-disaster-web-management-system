<template>
<div>
    <div>
      <PageTitle title='Estadisticas' subtitle='Estadisticas recolectadas por nuestra aplicacion'/>
    </div>
    <div class="container">
      <div class="chart1"><DoughnutChart></DoughnutChart></div>
      <div class="chart2"><UserChart></UserChart></div>
    </div>
</div>
</template>

<script>
import DoughnutChart from '../components/DoughnutChart'
import UserChart from '../components/UserChart'
import PageTitle from '../components/PageTitle.vue'


export default {
  name: 'Estadisticas',
  components: { DoughnutChart, PageTitle, UserChart },
};
</script>

<style>

.container {
  display: flex;
  width: 100%;
  height: 100%px;
  align-self: center;
}
.chart1,
.chart2 {
  width: 40%;
}

.chart1{
  height: 200px;
  border-radius: 5px;
}
</style>
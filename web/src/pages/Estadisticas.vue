<template>
<div>
    <div>
      <PageTitle title='Estadisticas' subtitle='Estadisticas recolectadas por nuestra aplicacion'/>
    </div>
    <div class="chartcontainer">
      <div class="chart1"><ComplaintChart></ComplaintChart></div>
      <div class="chart2"><UserChart></UserChart></div>
    </div>
</div>
</template>

<script>
import ComplaintChart from '../components/ComplaintChart'
import UserChart from '../components/UserChart'
import PageTitle from '../components/PageTitle.vue'


export default {
  name: 'Estadisticas',
  components: { ComplaintChart, PageTitle, UserChart },
};
</script>

<style>
.chartcontainer {
  display: flex;
  width: 100%;
  height: 150%;
  margin-left: 150px;
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
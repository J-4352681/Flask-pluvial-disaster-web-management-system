<template>
<div>
    <p>Estadisticas</p>
    <div> 
    <PlanetChart/>
    </div>
</div>
</template>

<script>
import PlanetChart from '../components/DoughnutChart'

export default {
  name: 'Estadisticas',
  components: { PlanetChart },
};
</script>


<style>

</style>
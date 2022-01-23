<template>
  <div>
    <canvas id="c-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import axios from 'axios';
import complaintsChartData from '../complaints-data.js'

export default {
  name: 'ComplaintsChart',
  data() {
    return {
      complaintsChartData
    }
  },
  mounted() {
    const ctx = document.getElementById('c-chart');
    axios.get('/estadisticas');
    new Chart(ctx, this.complaintsChartData);
  }
}
</script>
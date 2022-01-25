<template>
  <div>
    <p>Cantidad de denuncias por usuario</p>
    <canvas id="u-chart"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";
import {userChartData} from "../complaints-data.js";
import randomColor from "randomcolor";

export default {
  name: "UserChart",
  async mounted() {
    let a = await userChartData();
    const ctx = document.getElementById("u-chart");
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: Object.keys(a),
        datasets: [
          {
            label: 'Denuncias',
            data: Object.values(a).map((denuncias) => denuncias.denuncias),
            backgroundColor: Object.values(a).map((val) => randomColor(val)),
            borderColor: "Gray",
            borderWidth: 3,
          },
        ],
      },
    });
  },
};
</script>

<style>
#u-chart {
    box-shadow: 0 0 10px #e3e3e3;
}
</style>
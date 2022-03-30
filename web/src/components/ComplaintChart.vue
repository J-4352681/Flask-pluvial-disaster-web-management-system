<template>
  <div>
    <p>Cantidad de denuncias por categoria</p>
    <canvas id="c-chart"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";
import { complaintsChartData } from "../complaints-data.js";
import randomColor from "randomcolor";

export default {
  name: "ComplaintsChart",
  async mounted() {
    let a = await complaintsChartData();
    const ctx = document.getElementById("c-chart");
    new Chart(ctx, {
      type: "pie",
      data: {
        labels: Object.keys(a),
        datasets: [
          {
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
#c-chart {
  box-shadow: 0 0 10px #e3e3e3;
}
</style>
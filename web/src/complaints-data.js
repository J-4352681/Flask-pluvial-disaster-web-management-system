export const planetChartData = {
    type: "doughnut",
    data: {
      labels: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
      datasets: [
        {
          label: "Planetary Mass (relative to the Sun x 10^-6)",
          data: [0.166, 2.081, 3.003, 0.323, 954.792, 285.886, 43.662, 51.514],
          backgroundColor: "rgba(71, 183,132,.5)",
          borderColor: "#47b784",
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
    }
  };
  
  export default planetChartData;
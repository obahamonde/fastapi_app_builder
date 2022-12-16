<template>
    <div>
      <canvas id="planet-chart"></canvas>
    </div>
<div>{{foo}}</div>
</template>  
  <script setup lang="ts">
import { propsToAttrMap } from "@vue/shared";
import Chart from "chart.js";
const props = defineProps({
  chartType: {
    type: String,
    default: "line"
  }
});
const dataSet = ref({
  type: props.chartType,
  data: {
    labels: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    datasets: [
      {
        label: "Number of Moons",
        data: [0, 0, 1, 2, 79, 82, 27, 14],
        backgroundColor: "#ff0000",
        borderColor: "#0000ff",
        borderWidth: 3
      },
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
    lineTension: 1,
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
            padding: 25
          }
        }
      ]
    }
  }
});
const foo = ref("")
onMounted(async()=>{
    const ctx = document.getElementById('planet-chart');
    new Chart(ctx, dataSet.value);
    const { data } = await useFetch("/api/ApiReq/")
    foo.value = JSON.stringify(unref(data))
})
</script>
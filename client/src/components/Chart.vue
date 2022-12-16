<template>
 <select v-model="chartType" btn-get text-center>
      <option value="bar">Bar</option>
      <option value="line">Line</option>
      <option value="radar">Radar</option>
      <option value="doughnut">Doughnut</option>
      <option value="polarArea">Polar Area</option>
      <option value="bubble">Bubble</option>
      <option value="scatter">Scatter</option>
    </select> 
 <div id="canvasContainer">
      <canvas id="planet-chart"></canvas>
    </div>
<div>{{foo}}</div>
</template>  
  <script setup lang="ts">
import { Ref } from 'vue';
import Chart from "chart.js";
const chartType = ref("bar");
const foo = ref() as Ref<object>;
const dataSet = ref({
  type: computed(() => chartType.value),
  data: {
    labels: ["2XX", "3XX", "4XX", "5XX"],
    datasets: [
      {
        label: "Requests by Status Code",
        data: [12, 19, 3, 5],
        backgroundColor: "#ff0000",
        borderColor: "#0000ff",
        borderWidth: 3
      },
      {
        label: "Requests over Time",
        data: [2, 29, 5, 5],
          
        
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
const chart = ref(null) as Ref<Chart | null>;
const fetchChartData = async()=>{
  const { data } = await useFetch("/api/chart/");
  const dataSet = unref(data) as object;
  foo.value = dataSet;
}
  onMounted(async() => {
  chart.value = new Chart("planet-chart", unref(dataSet))
  await fetchChartData();
});
watch(chartType, () => {
  const el = document.getElementById("planet-chart") as HTMLCanvasElement;
  el.parentNode?.removeChild(el);
  const canvas = document.createElement("canvas");
  canvas.id = "planet-chart";
  document.getElementById("canvasContainer")?.appendChild(canvas);
  chart.value = new Chart("planet-chart", unref(dataSet));
});
  </script>
  
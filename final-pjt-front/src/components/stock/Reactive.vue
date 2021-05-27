<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  props: {
    resdataday: Array,
    resdataclose: Array,
  },
  data() {
    return {
      datacollection: null,
    };
  },
  created() {
    this.fillData();
  },
  mounted() {
    this.renderChart(this.datacollection, this.options);
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: this.resdataday,
        datasets: [
          {
            label: "거래량",
            backgroundColor: "#f87979",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#249EBF",
            data: this.resdataclose,
          },
        ],
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: false,
                },
                gridLines: {
                  display: true,
                },
              },
            ],
            xAxes: [
              {
                gridLines: {
                  display: false,
                },
              },
            ],
          },
          legend: {
            display: true,
          },
          responsive: true,
          maintainAspectRatio: false,
        },
      };
    },
    chartData() {
      return this.resdata;
    },
  },
};
</script>


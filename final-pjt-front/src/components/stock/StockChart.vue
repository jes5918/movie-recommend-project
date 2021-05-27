<script>
import { Line, mixins } from "vue-chartjs";

export default {
  components: { Line },
  mixins: [mixins.reactiveProp],
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
};
</script>
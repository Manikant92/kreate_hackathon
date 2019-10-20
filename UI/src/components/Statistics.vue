
<template>
    <div id="statics-container">
        <div id="numbers" class="column">
            <h2>Numbers</h2>
            <h3 class="stat-color stat-color-1"><b>Total No. of Customers:</b> {{ stats.totalCount }}</h3>
            <h3 class="stat-color stat-color-2"><b>Matched Customers: </b>{{ stats.allMatches }}</h3>
            <h3 class="stat-color stat-color-3"><b>Name Mismatch: </b>{{ stats.nameMismatch }}</h3>
            <h3 class="stat-color stat-color-4"><b>DOB Mismatch: </b>{{stats.dobMismatch }}</h3>
            <h3 class="stat-color stat-color-5"><b>Complete Mismatch: </b>{{ stats.completeMismatch }}</h3>  
        </div>
        <div id="statistics" class="column">
            <h2>Statistics</h2>
            <div id="chart">

            </div>
        </div>
    </div>
</template>
<script>
import ApexCharts from 'apexcharts';

export default {
   data() { 
    return {
      creatingChart: true,
    }
  },
  props: ['stats'],
  mounted() {
      this.createChart();
  },

  methods: {
      async createChart() {
          var options = {
            chart: {
                width: 400,
                type: 'pie',
            },
            labels: ['Matches', 'Name Mistmatches', 'DOB Mismatches', 'Complete Mismatch'],
            series: [this.stats.allMatchP || 0, this.stats.nameMismatchP || 0, this.stats.dobMismatchP || 0, this.stats.completeMismatchP || 0],
            responsive: [{
                breakpoint: 480,
                options: {
                    chart: {
                        width: 200
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }]
        }

        var chart = new ApexCharts(
            document.querySelector("#chart"),
            options
        );

        chart.render();

      }
  }
}

</script>
<style scoped>
.showing-records {
    font-size: 12px;
    font-weight: 500;
    opacity: 0.6;
}

.remarks {
    font-size: 12px;
}
</style>
<style scoped>
div#statics-container {
    display: flex;
    align-items: stretch;
    flex-wrap: wrap;
    margin-bottom:30px;
}

div#statics-container .column {
    background: #fff;
    width: 49%;
    padding: 25px 25px;
}

div#statics-container .column:last-child {
    margin-left: 2%;
}

#statics-container h2 {
    font-size: 20px;
}

#statics-container h3 {
    font-size: 16px;
    margin-bottom: 20px;
    font-weight: 400;
}

#statics-container h3.stat-color {
    padding-left: 25px;
    position: relative;
}

#statics-container h3.stat-color:before {
    position: absolute;
    content: '';
    width: 12px;
    height: 12px;
    background: aqua;
    left: 0;
    top: -1px;
    bottom: 0;
    margin: auto;
}

#statics-container h3.stat-color.stat-color-2:before {
    background:#4A90FB;
}

#statics-container  h3.stat-color.stat-color-3:before {
    background:#6FE397;
}

#statics-container  h3.stat-color.stat-color-4:before {
    background:#F0AF19;
}

#statics-container  h3.stat-color.stat-color-5:before {
    background:#E7415E;
}


</style>
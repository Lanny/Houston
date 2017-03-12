;(function() {
  function wrap(d3, ViewsChart) {
    var viewsChart = new ViewsChart(d3.select('.views-chart'));
  }

  define([
    'd3',
    'views-chart'
  ], wrap);
})();

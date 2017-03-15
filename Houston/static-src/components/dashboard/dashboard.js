;(function() {
  function wrap($, d3, ViewsChart) {
    var viewsChart = new ViewsChart($('.views-chart'));
  }

  define([
    'jquery',
    'd3',
    'views-chart'
  ], wrap);
})();

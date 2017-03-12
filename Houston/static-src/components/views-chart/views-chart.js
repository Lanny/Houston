;(function() {
  function wrap(d3, ajax, LineChart) {
    function formatDate(d) {
      return d.getFullYear() + '-' + d.getMonth() + '-' + d.getDay() + ' ' +
        d.getHours() + ':' + d.getMinutes();
    }

    function ViewsChart(container) {
      var self = this;
      self._container = container;
      self.init();
    }

    ViewsChart.prototype = {
      init: function() {
        var self = this;

        ajax.get('page-views', {
          granularity: 'day',
          start_time: formatDate(new Date(Date.now() - 1000 * 60 * 60 * 24 * 7)),
          end_time: formatDate(new Date(Date.now()))
        }).done(function(data) {
          var chart = new LineChart(self._container.select('svg'));
          var views = data.viewCounts.map(function(d) {
              return {
                date: new Date(d.bucket * 1000),
                value: d.count
              };
            });

          chart.addLine('views', views)
            .render();
        });
      }
    };

    return ViewsChart
  }

  define([
    'd3',
    'ajax',
    'line-chart'
  ], wrap);
})();


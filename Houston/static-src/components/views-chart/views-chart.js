;(function() {
  function wrap($, d3, ajax, LineChart) {
    var SECOND = 1000,
      MINUTE = SECOND * 60,
      HOUR = MINUTE * 60,
      DAY = HOUR * 24,
      WEEK = DAY * 7,
      MONTH = DAY * 28;

    var timeDeltaOptMap = {
      'day': DAY,
      'week': WEEK,
      'month': MONTH
    };

    function formatDate(d) {
      return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate() +
        ' ' + d.getHours() + ':' + d.getMinutes();
    }
    window.fd = formatDate;

    function getEndTime(deltaName, startTime) {
      startTime = (startTime === undefined) ? new Date() : startTime;


    }

    function ViewsChart(container) {
      var self = this;
      self._container = container;
      self._granularitySelect = self._container.find('select.granularity');
      self._timePeriodSelect = self._container.find('select.time-period');

      self._granularity = self._granularitySelect.val();
      self._startDate = new Date(
        Date.now() - timeDeltaOptMap[self._timePeriodSelect.val()]);
      self._endDate = new Date();
      self._chart = null;

      self.init();
    }

    ViewsChart.prototype = {
      init: function() {
        var self = this;

        self.bindHandlers();
        self.renderChart();
      },
      _getChart: function() {
        var self = this;

        if (!self._chart) {
          var d3Element = d3.select(self._container.find('svg')[0]);
          self._chart = new LineChart(d3Element);
        }

        return self._chart;
      },
      bindHandlers: function() {
        var self = this;
        self._container.find('select.granularity')
          .on('change', function(e) {
            var select = $(this);
            self._granularity = select.val();
            self.renderChart();
          });

        self._container.find('select.time-period')
          .on('change', function(e) {
            var select = $(this),
              timeDelta = timeDeltaOptMap[select.val()];
            self._startDate = new Date(Date.now() - timeDelta);
            self.renderChart();
          });
      },
      renderChart: function() {
        var self = this;

        ajax.get('page-views', {
          granularity: self._granularity,
          start_time: formatDate(self._startDate),
          end_time: formatDate(self._endDate)
        }).done(function(data) {
          var views = data.viewCounts.map(function(d) {
              return {
                date: new Date(d.bucket * 1000),
                value: d.count
              };
            });

          self._getChart()
            .clearLines()
            .addLine('views', views)
            .render();
        });
      }
    };

    return ViewsChart;
  }

  define([
    'jquery',
    'd3',
    'ajax',
    'line-chart'
  ], wrap);
})();


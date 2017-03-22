;(function() {
  function wrap(d3, $) {
    function LineChart(svg) {
      var self = this;
      self._svg = svg;
      self._lines = {};
      self._xDomain = null;
    }

    LineChart.prototype = {
      addLine: function(name, data) {
        var self = this;
        self._lines[name] = data;
        return self;
      },
      clearLines: function() {
        var self = this;
        self._lines = {};
        self._svg.selectAll('*').remove();
        return self;
      },
      setXDomain: function(value) {
        var self = this;
        self._xDomain = value;
        return self;
      },
      getXDomain: function() {
        var self = this;
        return self._xDomain
      },
      render: function() {
        var self = this,
          margin = {top: 20, right: 20, bottom: 30, left: 50},
          width = +self._svg.attr("width") - margin.left - margin.right,
          height = +self._svg.attr("height") - margin.top - margin.bottom,
          g = self._svg
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        for (var lineName in self._lines) {
          var lineData = self._lines[lineName],
            x = d3.scaleTime().rangeRound([0, width]),
            y = d3.scaleLinear().rangeRound([height, 0]);

          var line = d3.line()
              .x(function(d) { return x(d.date); })
              .y(function(d) { return y(d.value); });

          x.domain(self.getXDomain());
          y.domain([0, d3.max(lineData, (d) => d.value)])

          g.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

          g.append("g")
            .call(d3.axisLeft(y));

          g.append("path")
            .datum(lineData)
            .attr("fill", "none")
            .attr("stroke", "steelblue")
            .attr("stroke-linejoin", "round")
            .attr("stroke-linecap", "round")
            .attr("stroke-width", 1.5)
            .attr("d", line);
        }

        return self;
      }
    };

    return LineChart;
  }

  define([
    'd3',
    'jquery'
  ], wrap);
})();

;(function() {
  function wrap(d3, $) {
    function LineChart(svg) {
      var self = this;
      self._svg = svg;
      self._lines = {};
    }

    LineChart.prototype = {
      addLine: function(name, data) {
        var self = this;
        self._lines[name] = data;
        return self;
      },
      render: function() {
        var self = this,
          margin = {top: 20, right: 20, bottom: 30, left: 50},
          width = +self._svg.attr("width") - margin.left - margin.right,
          height = +self._svg.attr("height") - margin.top - margin.bottom,
          g = self._svg
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        var x = d3.scaleTime().rangeRound([0, width]),
          y = d3.scaleLinear().rangeRound([height, 0]);

        var line = d3.line()
            .x(function(d) { return x(d.date); })
            .y(function(d) { return y(d.value); });


        var combinedDates = [],
          combinedVals = [];

        for (var lineName in self._lines) {
          var lineData = self._lines[lineName];
          for (var i=0; i<lineData.length; i++) {
            combinedDates.push(lineData[i].date);
            combinedVals.push(lineData[i].value);
          }
        }

        x.domain(d3.extent(combinedDates));
        y.domain(d3.extent(combinedVals));

        g.append("g")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x));

        g.append("g")
          .call(d3.axisLeft(y))

        for (lineName in self._lines) {
          console.log(self._lines[lineName]);
          g.append("path")
            .datum(self._lines[lineName])
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

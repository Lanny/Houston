;(function() {
  function wrap($) {
    if (!('houstonConfig' in window)) {
      throw new Error('Improperly configured.');
    }

    function lookupEndpoint(name) {
      var endpoint = window.houstonConfig.endpoints[name];

      if (!endpoint) {
        throw new Error('Could not locate endpoint named: ' + name);
      }

      return endpoint;
    }

    var Module = {
      get: function(endpointName, options) {
        var url = lookupEndpoint(endpointName);

        return $.getJSON(url, options);
      }
    };

    return Module;
  }

  define([
    'jquery'
  ], wrap);
})();

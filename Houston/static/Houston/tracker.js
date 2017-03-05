;(function() {
  function encodePostData(data) {
    var pairs = [];
    for (var key in data) {
      pairs.push(encodeURIComponent(key) + '=' + encodeURIComponent(data[key]));
    }

    return pairs.join('&');
  }

  window.addEventListener('load', function() {
    var data = {
      path: document.location.pathname,
      csrfmiddlewaretoken: window._houston.csrfToken
    };
    var xhr = new XMLHttpRequest();
    xhr.open('POST', window._houston.pageViewURL, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send(encodePostData(data));
  });
})();

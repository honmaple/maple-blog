function dispatch() {
  var q = document.getElementById("search");
  if (q.value !== "") {
    var url = 'https://www.google.com/search?q=site:honmaple.com%20' + q.value;
    if (navigator.userAgent.indexOf('iPad') > -1 || navigator.userAgent.indexOf('iPod') > -1 || navigator.userAgent.indexOf('iPhone') > -1) {
      location.href = url;
    } else {
      window.open(url, "_blank");
    }
    return false;
  } else {
    return false;
  }
}

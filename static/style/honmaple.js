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
$(document).ready(function(){
  $('div#archive-list').click(function() {
    $('#hidelist').toggle();
    var i = $("div#archive-list").children('i');
    if (i.hasClass('fa-angle-double-down')) {
      $("div#archive-list").attr('title','close');
      i.removeClass('fa-angle-double-down');
      i.addClass('fa-angle-double-up');
    } else {
      $("div#archive-list").attr('title','open');
      i.removeClass('fa-angle-double-up');
      i.addClass('fa-angle-double-down');
    }
  });
  $('div#tag-archive-list').click(function() {
    $('#tag-hidelist').toggle();
    var i = $("div#tag-archive-list").children('i');
    if (i.hasClass('fa-angle-double-down')) {
      $("div#tag-archive-list").attr('title','close');
      i.removeClass('fa-angle-double-down');
      i.addClass('fa-angle-double-up');
    } else {
      $("div#tag-archive-list").attr('title','open');
      i.removeClass('fa-angle-double-up');
      i.addClass('fa-angle-double-down');
    }
  });
});

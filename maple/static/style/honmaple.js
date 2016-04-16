$(document).ready(function(){
  $("#showerror").hide();
  $('button#hide').click(function(){
    $("#showerror").hide();
  });
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", g.csrftoken);
      }
    }
  });
});
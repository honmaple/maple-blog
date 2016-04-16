$(document).ready(function(){
  $('a#clickCode').click(function() {
    $("#changeCode").attr("src","/validcode?code=" + Math.random());
  });
  $('button#login').click(function() {
    $.ajax ({
      type : "POST",
      url : url.login,
      data:JSON.stringify({
        name: $('input[name="name"]').val(),
        passwd: $('input[name="passwd"]').val(),
        code:$("#code").val()
      }),
      contentType: 'application/json;charset=UTF-8',
      success: function(result) {
        if (result.judge == true)
        {
          window.location = url.index;
        }
        else
        {
          $("#showerror").show();
          $("#error").text(result.error);
        }
      }
    });
  });
  $('button#register').click(function() {
    $.ajax ({
      type : "POST",
      url : url.register,
      data:JSON.stringify({
        name: $('#name').val(),
        email: $('#email').val(),
        passwd: $('#passwd').val(),
        code:$("#code").val()
      }),
      contentType: 'application/json;charset=UTF-8',
      success: function(result) {
        if (result.judge == true)
        {
          window.location = url.index;
        }
        else
        {
          $("#showerror").show();
          $("#error").text(result.error);
        }
      }
    });
  });
  $('button#forget').click(function() {
    $.ajax ({
      type : "POST",
      url : url.forget,
      data:JSON.stringify({
        confirm_email: $('#confirm_email').val(),
        code:$("#code").val()
      }),
      contentType: 'application/json;charset=UTF-8',
      success: function(result) {
        if (result.judge == true)
        {
          window.location = url.index;
        }
        else
        {
          $("#showerror").show();
          $("#error").text(result.error);
        }
      }
    });
  });
});
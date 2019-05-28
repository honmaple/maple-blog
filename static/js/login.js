$(document).ready(function(){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", g.csrftoken);
            }
        }
    });

    $('#username').focus(function() {
        var p = $(this).parent();
        if (p.hasClass("has-error")) {
            p.removeClass("has-error");
        }
    });
    $('#password').focus(function() {
        var p = $(this).parent();
        if (p.hasClass("has-error")) {
            p.removeClass("has-error");
        }
    });
    $('#entry-login').click(function() {
        var username = $('#username').val();
        var password = $('#password').val();
        if (username === ""){
            $('#username').parent().addClass("has-error");
            return;
        }
        if (password === "") {
            $('#password').parent().addClass("has-error");
            return;
        }
        $.ajax ({
            type: "POST",
            url: "/login",
            data: JSON.stringify({
                username: $('#username').val(),
                password: $('#password').val(),
                remember:  $("#remember").is(':checked')
            }),
            contentType: 'application/json;charset=UTF-8',
        }).done(function(response) {
            window.location.reload();
        }).fail(function(error) {
            alert(error.responseJSON.message);
        });
    });

});

$(document).ready(function(){
    $(document).on('click', '.entry-night-menu', function (e) {
        e.stopPropagation();
    });

    $('#entry-font-minus').click(function() {
        var zoomSize = $("html").css("zoom")
        var zoomScale = parseFloat(zoomSize) * 100 - 2
        if (zoomScale >= 80) {
            $("html").css("zoom", zoomScale + "%")
        }
        $("#entry-font-plus").removeClass("active")
        $("#entry-font").removeClass("active")
        $(this).addClass("active")
    });

    $('#entry-font-plus').click(function() {
        var zoomSize = $("html").css("zoom")
        var zoomScale = parseFloat(zoomSize) * 100 + 2
        if (zoomScale <= 120) {
            $("html").css("zoom", zoomScale + "%")
        }
        $("#entry-font-minus").removeClass("active")
        $("#entry-font").removeClass("active")
        $(this).addClass("active")
    });

    $('#entry-font').click(function() {
        $("html").css("zoom", "100%")
        $("#entry-font-minus").removeClass("active")
        $("#entry-font-plus").removeClass("active")
        $(this).addClass("active")
    });

    $('#entry-night-off').click(function() {
    });

    $('#entry-night-on').click(function() {
    });

    $("#entry-scale-minus").click(function() {
        $(".main").each(function(index) {
            $(this).css("max-width", "768px");
        });
        $(".footer").each(function(index) {
            $(this).css("max-width", "768px");
        });
        $(".entry-title").each(function(index) {
            $(this).toggleClass("text-center");
        });
        $("#entry-scale-plus").removeClass("active")
        $(this).addClass("active")
    });

    $("#entry-scale-plus").click(function() {
        $(".main").each(function(index) {
            $(this).css("max-width", "1024px");
        });
        $(".footer").each(function(index) {
            $(this).css("max-width", "1024px");
        });
        $(".entry-title").each(function(index) {
            $(this).toggleClass("text-center");
        });
        $("#entry-scale-minus").removeClass("active")
        $(this).addClass("active")
    });
});

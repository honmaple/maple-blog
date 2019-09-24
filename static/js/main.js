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
    $('[data-fancybox]').fancybox({
        protect: true
    });
    $("pre").css("max-height", $(window).height() * 0.8);
    var table = $("#text-table-of-contents").html();
    if (table) {
        $("#table-content").html(table);
        $("#table-content ul:first").addClass("nav");
        $("body").scrollspy({target: "#table-content"});
    }
    var top = $(".back-to-top");
    var tabs = $(".entry-tabs");
    $(window).on("scroll", function() {
        top.toggleClass("back-to-top-on", window.pageYOffset > 120);
        tabs.width($(".entry-tabs").width());
        tabs.toggleClass("entry-tabs-fixed", window.pageYOffset > 100);
    });
    top.click(function() {
        window.scrollTo(0, 0);
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

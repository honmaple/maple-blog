$(function() {
    if (!String.prototype.format) {
        String.prototype.format = function() {
            var args = arguments;
            return this.replace(/{(\d+)}/g, function(match, number) {
                return typeof args[number] != 'undefined'? args[number]: match;
            });
        };
    }
    var count = 0;
    function randomPoem() {
        $.ajax({
            type: "GET",
            url: "https://poem.honmaple.com/api/poem/random",
            dataType: "json",
            success: function (response) {
                var title = '<h3>{0}</h3>'.format(response.data.title);
                var author = '<p>{0}</p>'.format(response.data.author);
                var paragraphs = '<div>{0}</div>'.format(response.data.paragraphs.map(function(item) {
                    return "<p>{0}</p>".format(item);
                }).join(""));
                $(".entry-cover > .entry-cover-right > .entry-center").fadeOut(500, function() {
                    $(this).html(title + author + paragraphs).fadeIn(500);
                });
            }
        });
        count = count + 1;
        // setTimeout(randomPoem, 2000 + count * 1000);
    }
    if ($(window).width() > 600) {
        randomPoem();
    }
});

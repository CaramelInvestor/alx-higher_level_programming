$(document).ready(function() {
    const baseUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr"
    $.get(baseUrl, function(res){
        $("div#hello").text(res.hello)
    });
});

$(document).ready(function() {
    $("#toggle_header").click(function() {

        $("header").toggleClass("red green");

        if ($("header").hasClass("red")) {
            $("header").css("color", "#00FF00");

        } else if ($("header").hasClass("green")) {
            $("header").css("color", "#FF0000");
        }
    });
});

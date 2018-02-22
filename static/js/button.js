$(document).ready(function () {
    $("button").click(function () {
        $(".pop").fadeIn(300);
        positionPopup();
    });

    $(".pop > span, .pop").click(function () {
        $(".pop").fadeOut(300);
    });
});

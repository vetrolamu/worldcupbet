/**
 * Created by Alexey on 09.06.14.
 */

$(function(){


    //$("table.personal-stats tbody tr.available-to-bet").click(function(){

    //    window.location.href = "/bets/" + $(this).data("game-id");

    //});

    $('.make-bet-fast').editable();

    $("table.personal-stats tbody tr.available-to-score").find('.make-bet-fast').off();

    $("table.personal-stats tbody tr.available-to-score").click(function(){

        window.location.href = "/bets/game-score/" + $(this).data("game-id");

    });


    $('table.personal-stats tbody tr.available-to-bet td.fast-edit').on('click', function(e) {
        e.stopPropagation();
        $(this).parent().find('.make-bet-fast').editable("toggle");
    });

    $(".overall-scores-wrapper").smoothTouchScroll();

});

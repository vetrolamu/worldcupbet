/**
 * Created by Alexey on 09.06.14.
 */

$(function(){


$("table.personal-stats tbody tr.available-to-bet").click(function(){

    window.location.href = "/bets/" + $(this).data("game-id");

});$("table.personal-stats tbody tr.available-to-score").click(function(){

    window.location.href = "/bets/game-score/" + $(this).data("game-id");

});

$(".overall-scores-wrapper").smoothTouchScroll();


});

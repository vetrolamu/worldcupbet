/**
 * Created by Alexey on 09.06.14.
 */

$(function(){


$("table.personal-stats tbody tr.available-to-bet").click(function(){

    window.location.href = "/bets/" + $(this).data("game-id");

})



});

(function ($) {
    "use strict";

    var Score = function (options) {
        this.init('score', options, Score.defaults);
    };

    //inherit from Abstract input
    $.fn.editableutils.inherit(Score, $.fn.editabletypes.abstractinput);

    $.extend(Score.prototype, {

        render: function () {
            this.$input_winner = this.$tpl.find('input[name="winner"]:checked');
            this.$input_playoff = this.$tpl.find('input[name="is_playoff"]');
            this.$input_home = this.$tpl.find('input[name="home_ft_score"]');
            this.$input_visitor = this.$tpl.find('input[name="visitor_ft_score"]');
        },

        value2html: function (value, element) {
            var display_home_ft_score;
            var display_visitor_ft_score;
            var class_home_ft_score = "";
            var class_visitor_ft_score = "";
            if (value.home_ft_score){
               display_home_ft_score = value.home_ft_score;
               if (value.winner == 0){class_home_ft_score = "winner"}else if (value.winner == 1){class_home_ft_score = "loser"}

            } else{
               display_home_ft_score = "-";
            }
            if (value.visitor_ft_score){
               display_visitor_ft_score = value.visitor_ft_score;
               if (value.winner == 1){class_visitor_ft_score = "winner"}else if (value.winner == 0){class_visitor_ft_score = "loser"}

            } else{
               display_visitor_ft_score = "-";
            }
            var html = "" +
                "<span class = '" + class_home_ft_score + "'>" + display_home_ft_score + "</span> : <span class = '" + class_visitor_ft_score + "'>" + display_visitor_ft_score + "</span>";
            $(element).html(html);
        },

        html2value: function (html) {
            return null;
        },

        value2str: function (value) {
            var str = '';
            if (value) {
                for (var k in value) {
                    str = str + k + ' - ' + value[k] + ';';
                }
            }
            return str;
        },

        str2value: function (str) {
            return str;
        },

        value2input: function (value) {
            if (!value) {
                return;
            }
            if (value.is_playoff != 1){
                this.$tpl.find('input[name="winner"]').attr('type', 'hidden');
            }
            this.$tpl.find('input[name="winner"][value="'+value.winner+'"]').prop('checked', true);
            this.$input_playoff.val(value.is_playoff);
            this.$input_home.filter('[name="home_ft_score"]').val(value.home_ft_score);
            this.$input_visitor.filter('[name="visitor_ft_score"]').val(value.visitor_ft_score);
        },

        input2value: function () {
            return {
                winner: this.$tpl.find('[name="winner"]:checked').val(),
                is_playoff: this.$input_playoff.filter('[name="is_playoff"]').val(),
                home_ft_score: this.$input_home.filter('[name="home_ft_score"]').val(),
                visitor_ft_score: this.$input_visitor.filter('[name="visitor_ft_score"]').val()
            };
        },

        activate: function () {
            this.$input_home.filter('[name="home_ft_score"]').focus();
        }
    });

    Score.defaults = $.extend({}, $.fn.editabletypes.abstractinput.defaults, {
        tpl: '<div>' +
            '<input type = "radio" name = "winner" value = "0"><input type = "radio" name = "winner" value = "1"><div>' +
            '<span><input type = "hidden" name = "is_playoff" /></span>' +
            '<span>' +
            '<input type="number" name="home_ft_score">' +
            '</span>' +
            ' : ' +
            '<span>' +
            '<input type="number" name="visitor_ft_score">' +
            '</span>' +
            '<span>' +
            '</span></div></div>',

        inputclass: '',
        showbuttons: 'bottom' //WHY ISN'T THIS WORKING!!!
    });

    $.fn.editabletypes.score = Score;

}(window.jQuery));


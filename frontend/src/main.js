import {
	findTags,
	getValidLinks
} from "./scrape.js";
import {
	tag,
	createTip
} from "./single.js"

const root1 = "https://specbot.info/treehacks";

prepare();

var scrollTimer = null;

$(window).scroll(function () {
	if (scrollTimer) {
		clearTimeout(scrollTimer); // clear any previous pending timer
	}
	scrollTimer = setTimeout(prepare, 500);
});

function prepare() {
	scrollTimer = null;
	let i = 0;
	$("a").each(function () {
		i++
		(function (i, self) {
			setTimeout(function () {
				if ($(self).is('[news]'))
					return;
				if (checkVisible(self)) {
					console.log("fired")
					tag(self);
					if (!$(self).is("hasTip"))
						createTip(self);
					addMouseEnter(self);
				}
      }, 100*i);

		})(i, this)
	})

}

function checkVisible(elm) {
	var rect = elm.getBoundingClientRect();
	var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
	return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
}

function addMouseEnter(elm) {
<<<<<<< HEAD
	$(elm).mouseenter(function () {
		var checkExist = setInterval(function () {
			if ($('.tpd-tooltip').length) {
				clearInterval(checkExist);
				var bgColor = $('.tpd-tooltip').find('.political').css("background-color");
				bgColor = "#FFF";
				// $('.tpd-background-border-hack').css("border-color", bgColor);
				// $('.tpd-shift-stem-side-before').css("background-color", bgColor);
				// $('.tpd-shift-stem-side-after').css("background-color", bgColor);
				// $('.tpd-stem-border-corner').css("background-color", bgColor);

				// $('.tpd-stem-border-center').css("border", 0);

				$('.tpd-background-shadow').css("box-shadow", "0px 10px 25px 4px rgba(36, 36, 36, 0.4)");
				$('.tpd-stem-border-center-offset-inverse').css("filter", "drop-shadow(0px 1px 1px rgba(0, 0, 0, 0.4))");

				if ($('.tpd-stem-border-center').eq(3).is(":visible")) {
					$('.tpd-stem-border-center').css("border-right-color", bgColor); // Stem on left
				} else if ($('.tpd-stem-border-center').eq(0).is(":visible")) {
					$('.tpd-stem-border-center').css("border-bottom-color", bgColor);
				} else if ($('.tpd-stem-border-center').eq(1).is(":visible")) {
					$('.tpd-stem-border-center').css("border-left-color", bgColor); // Stem on right
					$('.tpd-stem-border-center-offset-inverse').css("filter", "drop-shadow(0px 5px 2px rgba(0, 0, 0, 0.4))");
				} else if ($('.tpd-stem-border-center').eq(2).is(":visible")) {
					$('.tpd-stem-border-center').css("border-top-color", bgColor);
				}

			}
		}, 100); // check every 100ms
	})
=======
  var checkExist = setInterval(function() {
     if ($('.tpd-tooltip').length) {
        clearInterval(checkExist);
        var bgColor = $('.tpd-tooltip').find('.political').css("background-color");
        bgColor = "#FFF";

        $('.tpd-background-shadow').css("box-shadow", "0px 10px 25px 4px rgba(36, 36, 36, 0.4)");
        $('.tpd-stem-border-center-offset-inverse').css("filter", "drop-shadow(0px 1px 1px rgba(0, 0, 0, 0.4))");

        if ($('.tpd-stem-border-center').eq(3).is(":visible")) {
          $('.tpd-stem-border-center').css("border-right-color", bgColor); // Stem on left
        }
        else if ($('.tpd-stem-border-center').eq(0).is(":visible")) {
          $('.tpd-stem-border-center').css("border-bottom-color", bgColor);
        }
        else if ($('.tpd-stem-border-center').eq(1).is(":visible")) {
          $('.tpd-stem-border-center').css("border-left-color", bgColor); // Stem on right
          $('.tpd-stem-border-center-offset-inverse').css("filter", "drop-shadow(0px 5px 2px rgba(0, 0, 0, 0.4))");
        }
        else if ($('.tpd-stem-border-center').eq(2).is(":visible")) {
          $('.tpd-stem-border-center').css("border-top-color", bgColor);
        }

     }
  }, 100); // check every 100ms
>>>>>>> fee9066b7ce2ce97bc2d6a8de515239114efb83c
}

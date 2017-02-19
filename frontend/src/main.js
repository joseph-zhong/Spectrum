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
	$("a").each(function () {
		if ($(this).is('[news]'))
			return;
		if (checkVisible(this)) {
			console.log("fired")
			tag(this);
			if (!$(this).is("hasTip"))
				createTip(this);
			addMouseEnter(this);
		}
	})
}

function checkVisible(elm) {
	var rect = elm.getBoundingClientRect();
	var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
	return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
}

function addMouseEnter(elm) {
	$(elm).mouseenter(function () {
		var checkExist = setInterval(function () {
			if ($('.tpd-tooltip').length) {
				clearInterval(checkExist);
				var bgColor = $('.tpd-tooltip').find('.political').css("background-color");
				bgColor = "#FFF";

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
}

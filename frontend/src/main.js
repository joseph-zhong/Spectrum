import {findTags,getValidLinks} from "./scrape.js";
import {createTips} from "./tooltip.js"

findTags();
createTips();

$("a[news='true']").mouseenter(function() {
  var checkExist = setInterval(function() {
     if ($('.tpd-tooltip').length) {
        clearInterval(checkExist);
        var bgColor = $('.tpd-tooltip').find('.political').css("background-color");
        $('.tpd-background-border-hack').css("border-color", bgColor);
        $('.tpd-shift-stem-side-before').css("background-color", bgColor);
        $('.tpd-shift-stem-side-after').css("background-color", bgColor);
        $('.tpd-stem-border-corner').css("background-color", bgColor);
        $('.tpd-stem-border-center').css("border-right-color", bgColor);

     }
  }, 100); // check every 100ms
})

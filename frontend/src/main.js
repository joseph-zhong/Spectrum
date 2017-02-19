import {findTags,getValidLinks} from "./scrape.js";
import {createTips} from "./tooltip.js"
import {tag,createTip} from "./single.js"

prepare();

var scrollTimer = null;

$(window).scroll(function() {
    if (scrollTimer) {
        clearTimeout(scrollTimer);   // clear any previous pending timer
    }
    scrollTimer = setTimeout(prepare,500);
});

function prepare(){
    scrollTimer = null;
    $("a").each(function(){
        if($(this).is('[news]'))
            return;
    if(checkVisible(this)){
        console.log("fired")
        tag(this);
        if(!$(this).is("hasTip"))
        createTip(this);
        }
    })

}

function checkVisible(elm) {
  var rect = elm.getBoundingClientRect();
  var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
  return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
}

$("a[news='true']").mouseenter(function() {
  var checkExist = setInterval(function() {
     if ($('.tpd-tooltip').length) {
        clearInterval(checkExist);
        var bgColor = $('.tpd-tooltip').find('.political').css("background-color");
        $('.tpd-background-border-hack').css("border-color", bgColor);
        $('.tpd-shift-stem-side-before').css("background-color", bgColor);
        $('.tpd-shift-stem-side-after').css("background-color", bgColor);
        $('.tpd-stem-border-corner').css("background-color", bgColor);


        // if (matchRGB($('.tpd-stem-border-center').css("border-right-color"))) {
        //   console.log("RIGHT");
        //   $('.tpd-stem-border-center').css("border-right-color", bgColor);
        // }
        // else if (matchRGB($('.tpd-stem-border-center').css("border-left-color"))) {
        //   console.log("LEFt");
        //   $('.tpd-stem-border-center').css("border-left-color", bgColor);
        // }
        // else if (matchRGB($('.tpd-stem-border-center').css("border-top-color"))) {
        //   console.log("TOP");
        //   $('.tpd-stem-border-center').css("border-top-color", bgColor);
        // }
        // else if (matchRGB($('.tpd-stem-border-center').css("border-bottom-color"))) {
        //   $('.tpd-stem-border-center').css("border-bottom-color", bgColor);
        //   console.log("BOTTOM");
        // }

     }
  }, 100); // check every 100ms
})

function matchRGB(check) {
  var arr = check.match(/^rgba?[\s+]?\([\s+]?(\d+)[\s+]?,[\s+]?(\d+)[\s+]?,[\s+]?(\d+)[\s+]?/i);
  return (arr[1] == "255" && arr[2] == "255" && arr[3] == "255");
}

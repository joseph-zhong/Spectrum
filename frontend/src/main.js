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
/**
 * Created by Joseph on 2/18/17.
 */

var currLink = window.location.href;
var links = document.getElementsByTagName('a');
for(var i=0; i < links.length; i++) {
    if (links[i].href.startsWith(currLink)
            && !links[i].href.contains('#')
            && links[i].href.length > currLink.length + 2) {
        console.log(links[i].href)
    }
}

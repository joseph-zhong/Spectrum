import {
	sites
} from "./sites.js"

//Labels all valid links with news="true"
export function findTags(doc) {
	console.log("Scraped");
	var article = $('a').map(function () {
		var link = $(this).attr('href');
		if (link) {
			if (checkValid(link)) {
                $(this).attr("news", true);
			}
		}
		return ($(this).attr('href'));
	})
}
//Gets all valid links
export function getValidLinks(){
    var validLinks = $('body').find('a[news="true"]').map(function(){
        return $(this).attr("href")
    }) 
    console.log(validLinks);
    return validLinks
}

export function getValidElements(){
    var validLinks = $('body').find('a[news="true"]').map(function(){
        return $(this)
    }) 
    return validLinks
}


const links = sites();

function checkValid(url) {
    url = url.toLowerCase();
	for (var i = 0; i < links.length; i++) {
		if (url.search(links[i]) != -1)
			return true;
	}
	return false;
}

// function checkValid(){
//     return true;
// }
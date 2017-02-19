import {
	sites
} from "./sites.js"

//Labels all valid links with news="true"
export function findTags(doc) {
	console.log("Scraped");
	var article = $('a').map(function () {
		var link = $(this).attr('href');
		if (link) {
            var val = checkValid(link);
			if (val) {
				$(this).attr("news", true);
                $(this).attr("site", val)
			}
		}
		return ($(this).attr('href'));
	})
}
//Gets all valid links
export function getValidLinks() {
	var validLinks = $('a[news="true"]').map(function () {
		return $(this).attr("href")
	})
	console.log(validLinks);
	return validLinks
}

export function getValidElements() {
	var validLinks = $('a[news="true"]').map(function () {
		return $(this)
	})
	return validLinks
}


const links = sites();

function checkValid(url) {
	url = url.toLowerCase();
	// if (url[0] == "/") {
	// 	var path = window.location.hostname
	// 	for (var i = 0; i < links.length; i++) {
	// 		if (path.search(links[i]) != -1)
	// 			return links[i];
	// 	}
	// }
	for (var i = 0; i < links.length; i++) {
		if (url.search(links[i]) != -1)
			return links[i];
	}
	return null;
}


// function checkValid(){
//     return true;
// }

import {
	sites
} from "./sites.js"

const root = "https://jsonplaceholder.typicode.com"


export function tag(e) {
	var link = $(e).attr('href');
	if (link) {
		var val = checkValid(link);
		if (val != 0) {
			$(e).attr("news", true);
			$(e).attr("site", val)
		} else {
			$(e).attr("news", false)
		}
	}
}

export function createTip(e) {
	if ($(e).attr('news') == "true") {
		$(e).attr("hasTip", "true")
		$.ajax({
			url: root + "/posts/1",
			method: "GET"
		}).then(function (data) {
			let bias = 3;
			let political;
			let politicHex;
			switch (bias) {
				case 1:
					political = "Liberal";
					politicHex = "#3751ff";
					break;
				case 2:
					political = "Moderate Liberal";
					politicHex = "#6fa0ff";
					break;
				case 3:
					political = "Neutral";
					politicHex = "#b265ff";
					break;
				case 4:
					political = "Moderate Conservative";
					politicHex = "#ff7070";
					break;
				case 5:
					political = "Conservative";
					politicHex = "#fe4d4d";
					break;
			}
			let val = data.body;
			let html = `
				<div class="box">
					<div class="political title" style="background-color: ${politicHex};">
						${political}
					</div>
		      		<div class="summary">
		        		<div class="title"> Summary </div>
		       		 		<p> ${val} </p>
		    	  	</div>
					<div class="related">
						<div class="title"> Related Articles </div>
						<p> Test </p>
					</div>
				</div>
				`
			Tipped.create($(e), html, {
				position: "right"
			});
		})
	}
}

const links = sites();

function checkValid(url) {
	url = url.toLowerCase();
	if (url[0] == "/") {
		var path = window.location.hostname
		for (var i = 0; i < links.length; i++) {
			if (path.search(links[i]) != -1)
				return links[i];
		}
	}
	for (var i = 0; i < links.length; i++) {
		if (url.search(links[i]) != -1)
			return links[i];
	}
	return 0;
}

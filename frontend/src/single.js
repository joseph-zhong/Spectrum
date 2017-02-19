import {
	sites
} from "./sites.js"

const root1 = "https://specbot.info/treehacks"
const root2 = "https://grandmaskittens.com"

export function tag(e) {
	var link = $(e).attr("href");
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
	if ($(e).attr("news") == "true") {
		$(e).attr("hasTip", "true")
		var text = Promise.resolve(
			$.ajax({
				url: root2 + "/spectrum?url=" + encodeURIComponent($(e).attr("href")),
				method: "GET"
			})
		)
		var related = Promise.resolve(
			{
				item: 1
			}
			// $.ajax({
			// 	url: root1,
			// 	method: "POST",
			// 	data: {
			// 		title: encodeURIComponent($(e).text())
			// 	},
			// 	dataType: "application/json; charset=utf-8"
			// })
		)
		var promises = Promise.all([text, related])
			.then(function (info) {
				let data = JSON.parse(info[0]);
				let bias = Math.round(data.weighted_average * 1.1);
				let political;
				let politicHex;
				switch (bias) {
					case -2:
						political = "Liberal";
						politicHex = "#3751ff";
						break;
					case -1:
						political = "Moderate Liberal";
						politicHex = "#6fa0ff";
						break;
					case 0:
						political = "Neutral";
						politicHex = "#b265ff";
						break;
					case 1:
						political = "Moderate Conservative";
						politicHex = "#ff7070";
						break;
					case 2:
						political = "Conservative";
						politicHex = "#fe4d4d";
						break;
				}
				let val = data.summary;
				console.log(data);
				data.suggestions = JSON.parse(data.suggestions);
				console.log(data);
				let source = data.brand;
				let title = data.title;
				let html = `
				<div class="box">
					<div class="political" style="background-color: ${politicHex};">
						<div class="title bigFont">
							${title}
						</div>
						<div class="source">
							${source} - ${political}
						</div>
					</div>
		      		<div class="summary">
		       		 	<p class="ourText"> ${val} </p>
		    	  	</div>
					  <hr>
						<div class="related">
			 				<div class="title"> Related Articles </div>`
			 		data.suggestions.forEach(function (item) {
						html += `<p class="ourText article">`
						html += `<a href="` + item.url + `">` + item.title + `</a>`
						html += `</p>`
					});

					html += `</div>
					</div>`
				Tipped.create($(e), html, {
					position: "right"
					// hideOn: false
				});
			}).catch(function(err){
				console.log(err);
			})
			// .catch(function (err) {
			// 	if (err.status != 200) {
			// 		console.log("FAILED")
			// 		console.log($(elm).text());
			// 		console.log(err);
			// 	} else {
			// 		var response = JSON.parse(err.responseText);
			// 		console.log(response);
			// 		var data = {
			// 			"weighted_average": 0,
			// 			"summary": "this is a great summary",
			// 			"brand": "New York Times",
			// 			"title": "McCain fights Trump"
			// 		}
			// 		// data = JSON.parse(info[0]);
			// 		let bias = Math.round(data.weighted_average * 1.1);
			// 		let political;
			// 		let politicHex;
			// 		switch (bias) {
			// 			case -2:
			// 				political = "Liberal";
			// 				politicHex = "#3751ff";
			// 				break;
			// 			case -1:
			// 				political = "Moderate Liberal";
			// 				politicHex = "#6fa0ff";
			// 				break;
			// 			case 0:
			// 				political = "Neutral";
			// 				politicHex = "#b265ff";
			// 				break;
			// 			case 1:
			// 				political = "Moderate Conservative";
			// 				politicHex = "#ff7070";
			// 				break;
			// 			case 2:
			// 				political = "Conservative";
			// 				politicHex = "#fe4d4d";
			// 				break;
			// 		}
			// 		let val = data.summary;
			// 		let source = data.brand;
			// 		let title = data.title;
			// 		let html = `
			// 		<div class="box">
			// 			<div class="political" style="background-color: ${politicHex};">
			// 				<div class="title bigFont">
			// 					${title}
			// 				</div>
			// 				<div class="source">
			// 					${source} - ${political}
			// 				</div>
			// 			</div>
			//       		<div class="summary">
			//        		 	<p class="ourText"> ${val} </p>
			//     	  	</div>
			// 			<div class="related">
			// 				<div class="title"> Related Articles </div>`
			// 		response.data.forEach(function (article) {
			// 			html += `<p class="ourText">`
			// 			html += `<a href="` + article[2] + `">` + article[0] + `</a>`
			// 			html += `</p>`
			// 		});

			// 		html += `</div>
			// 		</div>
			// 		`

			// 		console.log(html);
			// 		Tipped.create($(e), html, {
			// 			position: "right"
			// 			// hideOn: false
			// 		});
			// 	}
			// });
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

import {sites} from "./sites.js"

const root = "https://jsonplaceholder.typicode.com"


export function tag(e) {
	var link = $(e).attr('href');
	if (link) { 
		var val = checkValid(link);
		if (val != 0) {
			$(e).attr("news", true);
			$(e).attr("site", val)
		}
        else {
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
			let val = data.body;
			let html = `
		<div class="box">
			<div class="political">
				Liberal
			</div>
      <div class="summary">
          <h3> Summary </h3>
          <p> ${val} </p>
      </div>
			<div class="related">
				<h3> Related Articles </h3>
			</div>
		</div>
    `
			Tipped.create($(e), html, {
				position: "right"
			});
            $(e).css("background-color", "red");
			console.log("Phat tips");
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
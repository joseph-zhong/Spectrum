var root = "https://jsonplaceholder.typicode.com"

export function createTips() {
	var tips = $('a[news="true"]').map(function() {
		console.log("HMMM")
		var val = "This is a really really really really really really really really r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r long summary"
		var bias = 1;
		// Tipped.create($(this), "FUCK", {
		// 	position: "right"
		// });
		var self = $(this)
		$.ajax({
			url: root + "/posts/1",
			method: "GET"
		}).then(function(data) {
			val = data.body;
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
			Tipped.create($(self), html, {
				position: "right"
			});
			console.log("Phat tips")
		})
	})
}

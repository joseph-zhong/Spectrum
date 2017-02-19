var root = "https://jsonplaceholder.typicode.com"

export function createTips() {
	var tips = $('a[news="true"]').map(function() {
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

		var self = $(this)
		$.ajax({
			url: root + "/posts/1",
			method: "GET"
		}).then(function(data) {
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
			Tipped.create($(self), html, {
				position: "right"
			});
			console.log("Phat tips")
		})
	})
}

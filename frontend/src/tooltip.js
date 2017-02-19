var root = "https://jsonplaceholder.typicode.com"

export function createTips() {
	var tips = $('a[news="true"]').map(function() {
    let bias = 0;
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

		var self = $(this)
		$.ajax({
			url: root + "/posts/1",
			method: "GET"
		}).then(function(data) {

			Tipped.create($(self), html, {
				position: "right",
				hideOn: false
			});
			console.log("Phat tips")
		})
	})
}

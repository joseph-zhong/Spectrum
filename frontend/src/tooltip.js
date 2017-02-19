var root = "https://jsonplaceholder.typicode.com"

export function createTips() {
	var tips = $('a[news="true"]').map(function() {


		var self = $(this)
		$.ajax({
			url: root + "/posts/1",
			method: "GET"
		}).then(function(data) {
			
			Tipped.create($(self), html, {
				position: "right"
			});
			console.log("Phat tips")
		})
	})
}

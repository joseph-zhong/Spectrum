export function createTips() {
	var tips = $("a[news='true']").map(function () {
		console.log("HMMM")
		var val = "This is a really really really really really really really really r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r r long summary"
        var bias = 2;
        var bar = bias < 0 ? "rep" : "dem";

        var html = `
        <div class="box">
			<div class="text">
	            <div class="summary">
	                <h3> Summary </h3>
	                <p> ${val} </p>
	            </div>
				<div class="related">
					<h3> Related Articles </h3>
				</div>
			</div>
            <div class="data">
                <div class="bias">
                    <h3> Liberal </h3>
                    <div class="vertical>
                        <div id="back"> </div>
                        <div id="${bar}"> </div>
                    </div>
                    <h3> Conservative </h3>
                </dib>
            </div>
        </div>
        `
		Tipped.create($(this), html, {
			position: "right"
		});
	})
}

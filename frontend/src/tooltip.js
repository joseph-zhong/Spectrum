export function createTips() {
	var tips = $("a[news='true']").map(function() {
        console.log("HMMM")
        var val = "This is link"
        var html = `
        <div class="box">
            <div class="summaries">
                <h2> Title </h2>
                <h2> Subtext </h2>
            </div>
            <div class="data">
                <div class="bias">
                    <h3> Liberal </h3>
                    <h4> Progress </h4>
                    <h3> Conservaties </h3>
                </dib>
            </div>
        </div>
        `
        console.log(html)
        Tipped.create($(this), html,{
            position: "bottomleft"
        });
	})
}

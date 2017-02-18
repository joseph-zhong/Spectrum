import {
	getValidElements
} from "./scrape.js"


export function createTips() {
	var tips = $("a[news='true']").map(function () {
        console.log("HMMM")
        var val = "bel"
        var html = `
				<p>
            ${val}
				</p>
        `
        Tipped.create($(this), html, {
            position: "bottomleft"
        });
	})
}

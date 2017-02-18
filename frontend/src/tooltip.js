import {
	getValidElements
} from "./scrape.js"


export function createTips() {
	var tips = $("a[news='true']").map(function() {
        console.log("HMMM")
        var val = "This is link"
        var html = `
        <p>
            ${val}
        </p>
        `
        console.log(html)
        Tipped.create($(this), html,{
            position: "bottomleft"
        });
	})
}

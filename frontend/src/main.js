import {findTags,getValidLinks} from "./scrape.js";
import {createTips} from "./tooltip.js"

findTags();
console.log(getValidLinks());
createTips();

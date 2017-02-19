/**
 * Created by Joseph on 2/19/17.
 */


thing = {}
mapping = {
'Bias: Lean Left' : -1,
'Bias: Lean Rightt' : 1,
'Bias: Left' : -2,
'Bias: Right' : 2,
'Bias: Mixed' : 0,
'Bias: Center': 0,
}

var asdf = document.getElementsByClassName('views-field views-field-title source-title')
var imgs = document.getElementsByTagName('img')
real_imgs = []
for (var i = 0; i < imgs.length; i++) {
  if(imgs[i].hasAttribute('typeof') && imgs[i].getAttribute('typeof') == 'foaf:Image') {
	real_imgs.push(imgs[i])
  }
}

for (var i = 0; i < real_imgs.length; i++) {
  var bias = real_imgs[i].getAttribute('alt')
  console.log(bias)
  var score = mapping[bias]
  console.log(score)
  var title = asdf[i].children[0].innerHTML
  console.log(asdf[i].children[0])
  console.log(title)
  thing[title] = score
}

JSON.stringify(thing, null, 2)
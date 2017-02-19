var Nightmare = require('nightmare');

function getLeaning(article) {
  var cheerio = require('cheerio');
  var nightmare = Nightmare({ show: true });

  console.log(article);

  nightmare
    .goto(article)
    .wait('div#draggable > .media > .media-body > .media-headline > a')
    .evaluate(function () {
      return document.body.innerHTML;
    })
    .end()
    .then(function (result) {
      var $ = cheerio.load(result);
      var biasURL = $('div#draggable > .media > .media-body > .news-source > img').attr('src');

      switch (biasURL) {
        case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-left.png"):
          console.log("Left");
          return("-2");

        case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-leaning-left.png"):
          console.log("Lean Left");
          return("-1");

        case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-center.png"):
          console.log("Center");
          return("0");

        case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-leaning-right.png"):
          console.log("Lean Right");
          return("1");

        case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-right.png"):
          console.log("Right");
          return("2");
      }
    })
    .then(function (pol) {
      console.log(pol);
    })
    .catch(function (error) {
      console.error('Search failed:', error);
    });
}

getLeaning('http://www.allsides.com/gnp/tod/index32.php?q=Friends%20No%20More?%20Jorge%20P%C3%A9rez%20and%20Donald%20Trump')//, function(eval) {
  // console.log("LOOOL");
  // console.log(eval);
// }

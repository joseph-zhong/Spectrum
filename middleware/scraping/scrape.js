var Nightmare = require('nightmare');
var cheerio = require('cheerio');

function getLeaning(article, callback) {
  var SEARCH_QUERY = "http://www.allsides.com/gnp/tod/index32.php?q=";

  var nightmare = Nightmare({ show: true });

  var articleURL = SEARCH_QUERY + encodeURIComponent(article);

  nightmare
    .goto(articleURL)
    .wait('div#draggable > .media > .media-body > .media-headline > a')
    .evaluate(function () {
      return document.body.innerHTML;
    })
    .end()
    .then(function (result) {
      var $ = cheerio.load(result);
      var returnObj = {"-2": [], "-1": [], "0": [], "1": [], "2": [], "3": []};
      $('div.isotope-item').each(function(i, elem) {
        var tmpArr = [];
        var re = /(.+)(?:\s-\s)(.+)$/g;
        var tmpNum = getLeanNumber($(elem).find('.news-source > img').attr('src'));

        reRes = re.exec($(elem).find("h6.media-headline").text());
        tmpArr.push(reRes[1].trim(), reRes[2].trim(), $(elem).find("h6.media-headline > a").attr('href'));

        returnObj[tmpNum].push(tmpArr);
      })

      var articleNum = getLeanNumber($('div#draggable > .media > .media-body > .news-source > img').attr('src'));
      callback(articleNum, returnObj);
    })
    // .then(function (pol) {
    //   console.log(pol);
    // })
    .catch(function (error) {
      console.error('Search failed:', error);
    });
}

function getLeanNumber(biasURL) {
  switch (biasURL) {
    case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-left.png"):
      return("-2");

    case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-leaning-left.png"):
      return("-1");

    case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-center.png"):
      return("0");

    case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-leaning-right.png"):
      return("1");

    case ("http://www.allsides.com/sites/default/files/styles/bias144x24/public/bias-right.png"):
      return("2");

    default:
      return("3");
  }
}

function chooseArticle(num, similarArticles) {
  switch (num) {
    case "-2":
      if (similarArticles["0"].length != 0) {
        return similarArticles["0"].slice(0, 3);
      }
      else if (similarArticles["1"].length != 0) {
        return similarArticles["1"].slice(0, 3);
      }
      else if (similarArticles["-1"].length != 0) {
        return similarArticles["-1"].slice(0, 3);
      }
      return similarArticles["2"].slice(0, 3);
    case "-1":
      if (similarArticles["1"].length != 0) {
        return similarArticles["1"].slice(0, 3);
      }
      else if (similarArticles["0"].length != 0) {
          return similarArticles["0"].slice(0, 3);
      }
      return similarArticles["2"].slice(0, 3);
    case "0":
      var rand = Math.random();
      if (rand > 0.5 && similarArticles["1"].length != 0) {
        return similarArticles["1"].slice(0, 3);
      }
      else if (similarArticles["-1"].length != 0) {
        return similarArticles["-1"].slice(0, 3);
      }
      else if (rand > 0.5 && similarArticles["2"].length != 0) {
        return similarArticles["2"].slice(0, 3);
      }
      return similarArticles["-2"].slice(0, 3);
    case "1":
      if (similarArticles["-1"].length != 0) {
        return similarArticles["-1"].slice(0, 3);
      }
      else if (similarArticles["0"].length != 0) {
        return similarArticles["0"].slice(0, 3);
      }
      return similarArticles["-2"].slice(0, 3);
    case "2":
      if (similarArticles["0"].length != 0) {
        return similarArticles["0"].slice(0, 3);
      }
      else if (similarArticles["-1"].length != 0) {
        return similarArticles["-1"].slice(0, 3);
      }
      else if (similarArticles["1"].length != 0) {
        return similarArticles["1"].slice(0, 3);
      }
      return similarArticles["-2"].slice(0, 3);
    case "3":
      // Run Joseph's ML code
      return null;
  }
}

getLeaning('Friends No More? Jorge Pérez and Donald Trump', function(num, similarArticles) {
  console.log(chooseArticle(num, similarArticles));
})

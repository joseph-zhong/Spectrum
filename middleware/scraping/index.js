var express = require('express');
var app = express();
var scraper = require('./scrape.js');

app.get('/', function(req, res) {
  res.send('Welcome to Spectrum.');
})

app.post('/', function(req, res) {
  scraper.scrape(function(data) {
    console.log(data);
    res.json(data);
  });
})

app.listen('3000', function() {
  console.log("App listening on port 3000!!");
})

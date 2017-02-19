#!/usr/bin/env nodejs
var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var scraper = require('./scrape.js');

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));

app.get('/', function(req, res) {
  console.log("GET / Entered");
  res.send('Welcome to Spectrum.');
})

app.post('/', function(req, res) {
  console.log("POST / Entered");
  scraper.scrape(req.body.title, function(data) {
    console.log("Returned the following data:\n" + data);
    res.json(data);
  });
})

app.listen(process.env.PORT || 3000, function() {
  console.log("App listening on port 3000!!");
})

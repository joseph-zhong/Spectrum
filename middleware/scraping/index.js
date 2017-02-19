#!/usr/bin/env nodejs
var express = require('express');
var app = express();
var scraper = require('./scrape.js');

app.get('/', function(req, res) {
  console.log("GET / Entered");
  res.send('Welcome to Spectrum.');
})

app.post('/', function(req, res) {
  console.log("POST / Entered");
  scraper.scrape(function(data) {
    console.log(data);
    res.json(data);
  });
})

app.listen(process.env.PORT || 3000, function() {
  console.log("App listening on port 3000!!");
})

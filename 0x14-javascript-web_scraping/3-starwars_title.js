#!/usr/bin/node
/*
prints title of a Star Wars movie
*/
const request = require('request');

let id = process.argv[2];
let url = 'http://swapi.co/api/films/' + id;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let json = JSON.parse(body);
    console.log(json.title);
  }
});

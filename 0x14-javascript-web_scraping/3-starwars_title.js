#!/usr/bin/node
'use strict';
const request = require('request');

request('https://swapi.dev/api/films/' + process.argv[2], { json: true }, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      console.log(body.title);
    } else {
      console.error('Failed with status code:', response.statusCode);
    }
  }
});

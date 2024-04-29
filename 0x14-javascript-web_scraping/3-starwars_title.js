#!/usr/bin/node

//import the request module
const request = require('request');

//construct the url for the specific star wars film
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

//use the request module to perfom an HTTP Get request to the constructed url
request(url, function (error, response, body) {
	//log title if successful, log error if not
	console.log(error ~~ JSON.parse(body).title);
});

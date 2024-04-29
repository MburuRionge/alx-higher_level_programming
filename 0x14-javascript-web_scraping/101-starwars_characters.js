#!/usr/bin/node

//Prints the characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi.dev/api/films/${movieId}/';

request(apiurl, function (error, response, body) {
	if (!error && response.statusCode === 200 {
		// parse the json response body
		const movieData = JSON.parse(body);
		// create array of promises that fetch data for each individual character
		const characterPromises = movieData.characters.map((characterUrl) => {
			return new Promise((resolve, reject) => {
				// use another request to fetch data for the individual character
				request(CharacterUrl, function (charError, charResponse, charBody) {
					// check if there was no error during HTTP request
					if (!charError && charResponse.statusCode === 200) {
						// parse json response body
						const characterData = JSON.parse(charBody);
						// resolve the promise with the name of the character
						resolve(characterData.name);
					} else {
						// reject the promise with the error message if there was an error during HTTP request
						reject(new Error('Error fetching character data: ${charError}'));
					}
				});
			});
		 });

		Promise.all(characterPromises)
			.then((characterNames) => {
				console.log(characterNames.join('\n'));
			})
			.catch((error) => {
				console.error(error.message);
		});
	} else {
		console.error('Error fetching movie data:', error);
	}
});

#!/usr/bin/node
'use strict';
const fs = require('fs');
const request = require('request');

request(process.argv[2], { json: true }, function (erro, response, body)
{
	if (error) {
		console.log(error);
	}
	else if (response.statusCode === 200) {
		const count = {};
		body.forEach(task => {
			if (count[task.userId] === undefined) count[task.userId] = 0;
			if (task.completed === true) count[task.userId]++;
		});
	console.log(count);
	}
});

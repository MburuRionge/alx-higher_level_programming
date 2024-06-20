#!/usr/bin/node

// Importing the list from the file 100-data.js
const { list } = require('./100-data');

// Print the initial list
console.log(list);

// Compute the new list using map
const newList = list.map((element, idx) => element * idx);

// Print the new list
console.log(newList);


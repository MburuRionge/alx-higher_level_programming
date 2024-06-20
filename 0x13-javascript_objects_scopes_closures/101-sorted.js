#!/usr/bin/node

// Importing the dictionary from the file 101-data.js
const { dict } = require('./101-data');

// Convert the dictionary to an array of entries
const convertedArr = Object.entries(dict);

// Initialize the new object
const newDict = {};

// Loop through the array and populate the new object
convertedArr.forEach(([userId, occurence]) => {
  // If the value already exists in newObj, push the key to the array
  if (newDict[occurrence]) {
    newDict[occurrence].push(userId);
  } else {
    // Otherwise, create a new array with the key
    newDict[occurrence] = [userId];
  }
});

// Print the new object
console.log(newDict);

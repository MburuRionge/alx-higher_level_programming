#!/usr/bin/node
/*
reverses a list w/o builtin call reverse
*/
exports.esrever = function(list) {
  let result = [];

  // Check if list is an array
  if (!Array.isArray(list)) {
    throw new Error('Input is not an array');
  }

  // Traverse the list from the end to the beginning
  for (let i = list.length - 1; i >= 0; i--) {
    result.push(list[i]);
  }

  return result;
};

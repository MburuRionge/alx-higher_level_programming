#!/usr/bin/node

const fs = require('fs').promises;
const { argv } = require('process');

(async () => {
  try {
    // Read the first source file
    const data1 = await fs.readFile(argv[2], 'utf8');
    // Read the second source file
    const data2 = await fs.readFile(argv[3], 'utf8');
    // Concatenate the contents and write to the destination file
    await fs.writeFile(argv[4], data1 + data2, 'utf8');
  } catch (err) {
    console.error(err);
  }
})();

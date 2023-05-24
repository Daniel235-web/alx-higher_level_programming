#!/usr/bin/node

const fs = require('fs');

// Read the contents of the file
fs.readFile('path/to/your/file.js', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  // Modify the value of myVar to 333
  const modifiedData = data.replace(/const myVar = \d+;/, 'const myVar = 333;');

  // Write the modified contents back to the file
  fs.writeFile('path/to/your/file.js', modifiedData, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('Variable modified successfully!');
  });
});

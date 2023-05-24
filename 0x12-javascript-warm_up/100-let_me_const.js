#!/usr/bin/node

const fs = require('fs');

// Read the contents of the file
const filePath = 'path/to/your/file.js';
const fileContents = fs.readFileSync(filePath, 'utf8');

// Modify the value of myVar to 333
const modifiedContents = fileContents.replace(/const myVar = .+;/, 'const myVar = 333;');

// Write the modified contents back to the file
fs.writeFileSync(filePath, modifiedContents, 'utf8');

console.log('Variable modified successfully!');

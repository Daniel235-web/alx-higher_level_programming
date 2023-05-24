#!/usr/bin/node

const myVar = process.argv.slice(2);

if (myVar < 2) {
  console.log('No argument');
} else if (myVar.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

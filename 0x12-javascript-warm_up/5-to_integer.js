#!/usr/bin/node

const arg = process.argv[2];
const parsedInt = parseInt(arg);

if (!arg || isNaN(parsedInt)) {
  console.log('Not a number');
} else {
  console.log('My number:', parsedInt);
}

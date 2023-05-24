#!/usr/bin/node

const myvar = process.argv.slice(2);
const myLetter = 'X';
let i = 0;
const myarg = parseInt(process.argv[2]);

if (myvar.length === 0) {
  console.log('Missing size');
}
while (i < myarg) {
  console.log(myLetter.repeat(myarg));
  i++;
}

#!/usr/bin/node

const myVar = process.argv.slice(2);

if (myVar < 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}

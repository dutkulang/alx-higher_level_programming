#!/usr/bin/node

const number = process.argv[2];

if (process.argv.slice(2) > 1) {
  if (parseInt(number)) {
    console.log(`My number: ${parseInt(number)}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}

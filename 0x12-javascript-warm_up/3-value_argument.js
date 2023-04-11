#!/usr/bin/node

const count = process.argv.slice(2);

if (count < 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}

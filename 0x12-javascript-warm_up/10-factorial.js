#!/usr/bin/node

function fact (n) {
  if (process.argv.slice(2) < 1) {
    return 1;
  } else {
    if (n === 1) {
      return 1;
    }
    return n * fact(n - 1);
  }
}

const n = process.argv[2];

console.log(fact(n));

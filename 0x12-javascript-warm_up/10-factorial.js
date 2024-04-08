#!/usr/bin/node

const process = require('process');
const args = process.argv;
const firstArg = parseInt(args[2]);

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }

  if (a === 0) {
    return 1;
  }

  return a * factorial(a - 1);
}

console.log(factorial(firstArg));

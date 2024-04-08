#!/usr/bin/node

const str = 'C is fun';
const process = require('process');
const args = process.argv;
const val = parseInt(args[2]);

if (isNaN(val)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < val; i++) {
  console.log(str);
}

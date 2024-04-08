#!/usr/bin/node

const process = require('process');
const args = process.argv;
const val = parseInt(args[2]);

if (isNaN(val)) {
  console.log('Missing size');
}

for (let i = 0; i < val; i++) {
  let row = '';
  for (let j = 0; j < val; j++) {
    row += 'X';
  }
  console.log(row);
}

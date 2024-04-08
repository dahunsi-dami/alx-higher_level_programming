#!/usr/bin/node

const process = require('process');
const args = process.argv;
const val = args[2];

if (isNaN(val)) {
  console.log('Not a number');
} else if (typeof val === 'string') {
  const dec = parseInt(val);
  if (dec !== 'NaN') {
    console.log('My number:', dec);
  }
} else if (typeof val === 'number' && Number.isInteger(val)) {
  console.log('My number:', parseInt(val));
} else if (typeof val === 'number' && !Number.isNaN(val)) {
  console.log('My number:', Math.floor(parseInt(val)));
} else {
  console.log('Not a number');
}

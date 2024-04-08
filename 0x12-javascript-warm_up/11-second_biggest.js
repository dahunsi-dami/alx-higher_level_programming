#!/usr/bin/node

const { argv } = require('node:process');
const coll = [0];
let consid;
let stud = -Infinity;
let i = 2;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  while (i < argv.length) {
	consid = parseInt(argv[i]);
    if (consid > coll[0]) {
      stud = coll[0];
      coll[0] = consid;
      i++;
    } else {
      i++;
    }
  }
  console.log(stud);
}

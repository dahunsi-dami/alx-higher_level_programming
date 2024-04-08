#!/usr/bin/node

const { argv } = require('node:process');
const coll = [];
let consid;
let stud = -Infinity;
let i = 2;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  while (i < argv.length) {
    consid = parseInt(argv[i]);
    if (consid > coll[0] || coll.length === 0) {
      if (coll.length === 0) {
        coll[0] = consid;
      }
      stud = coll[0];
      coll[0] = consid;
    } else if (consid > stud && consid !== coll[0]) {
      stud = consid;
    }
    i++;
  }

  if (typeof stud === undefined) {
    stud = consid;
  }
  console.log(stud);
}

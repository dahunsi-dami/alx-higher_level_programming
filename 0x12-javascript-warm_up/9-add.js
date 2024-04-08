#!/usr/bin/node

const process = require('process');
const args = process.argv;
const firstArg = parseInt(args[2]);
const secondArg = parseInt(args[3]);

function add (a, b) {
  console.log(a + b);
}

add(firstArg, secondArg);

#!/usr/bin/node

const process = require('process');
const args = process.argv;
const subArg = args[2];
const adjArg = args[3];

console.log(subArg + ' is ' + adjArg);

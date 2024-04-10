#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

const fArg = argv[2];
const sArg = argv[3];
const tArg = argv[4];

const fExists = fs.existsSync(fArg);
const sExists = fs.existsSync(sArg);

if (fExists && sExists) {
  const fRead = fs.readFileSync(fArg, 'utf8');
  const sRead = fs.readFileSync(sArg, 'utf8');
  const tRead = `${fRead}${sRead}`;

  fs.writeFileSync(tArg, tRead);
}

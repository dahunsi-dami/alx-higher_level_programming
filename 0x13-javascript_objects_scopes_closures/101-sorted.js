#!/usr/bin/node

const { dict } = require('./101-data');

const d = Object.entries(dict).reduce((acc, [k, v]) => {
  acc[v] = acc[v] || [];
  acc[v].push(k);
  return acc;
}, {});

console.log(d);

/* let d = {};

for (const key in dict) {
  if (!(dict[key] in d)) {
    d[dict[key]] = [];
  }
}

for (const k in d) {
  for (const ki in dict) {
    if (parseInt(k) === dict[ki]) {
      d[k].push(ki);
    }
  }
}

console.log(d); */

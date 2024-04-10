#!/usr/bin/node

const firstSquare = require('./5-square');

class Square extends firstSquare {
  charPrint (c) {
    let bluck = 'C';

    if (typeof c === 'undefined') {
      bluck = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += bluck;
      }
      console.log(row);
    }
  }
}

module.exports = Square;

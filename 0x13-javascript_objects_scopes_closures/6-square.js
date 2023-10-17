#!/usr/bin/node
const SquareParent = require('./5-square.js');

const Square = class Square extends SquareParent {
  charPrint (c) {
    if (c) {
      let line = '';
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.height; i++) {
          line += c;
        }
        console.log(line);
        line = '';
      }
    } else {
      super.print();
    }
  }
};

module.exports = Square;

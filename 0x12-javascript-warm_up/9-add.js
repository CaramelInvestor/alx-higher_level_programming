#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const firstNum = process.argv[2];
const secondNum = process.argv[3];

if (!isNaN(firstNum) && !isNaN(secondNum)) {
  const result = add(parseInt(firstNum, 10), parseInt(secondNum, 10));
  console.log(result);
} else {
  console.log('NaN');
}

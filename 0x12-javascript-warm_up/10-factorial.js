#!/usr/bin/node
function printFactorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * printFactorial(n - 1);
  }
}

const args = process.argv[2];

console.log(printFactorial(args));

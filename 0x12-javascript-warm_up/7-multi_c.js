#!/usr/bin/node
const args = process.argv[2];
const number = parseInt(args);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;

  while (i < number) {
    console.log('C is fun');
    i++;
  }
}

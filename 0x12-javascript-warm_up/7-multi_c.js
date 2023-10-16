#!/usr/bin/node
const args = process.argv[2];
if (args.length === 0 || isNaN(parseInt(args[0]))) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(args[0]);
  let i = 0;

  while (i < x) {
    console.log('C is fun');
    i++;
  }
}

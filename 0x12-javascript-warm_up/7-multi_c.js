#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(args[0], 10)
  let i = 0;

  while (i < x) {
  console.log('C is fun');
  i++;
}
}
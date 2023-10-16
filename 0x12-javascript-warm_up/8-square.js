#!/usr/bin/node
const args = process.argv[2];
if (args.length === 0 || isNaN(args[0])) {
  console.log('Missing size');
} else {
  const x = parseInt(args[0], 10);

  for (let i = 0; i < x; i++) {
    let line = '';
    for (let j = 0; j < x; j++) {
        line += 'X';
    }
    console.log(line);
  }
}

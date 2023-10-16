#!/usr/bin/node
const args = process.argv[2];
if (args === undefined || isNaN(args[0])) {
  console.log('Missing size');
} else {
  const x = parseInt(args, 10);

  for (let i = 0; i < x; i++) {
    let line = '';
    for (let j = 0; j < x; j++) {
        line += 'X';
    }
    console.log(line);
  }
}

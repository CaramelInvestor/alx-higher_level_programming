#!/usr/bin/node

let num = process.argv[2];

if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

// const args = process.argv[2];
// if (args.length === 0 || isNaN(args[0])) {
//   console.log('Missing number of occurrences');
// } else {
//   const x = parseInt(args[0], 10)
//   let i = 0;

//   while (i < x) {
//   console.log('C is fun');
//   i++;
// }
// }
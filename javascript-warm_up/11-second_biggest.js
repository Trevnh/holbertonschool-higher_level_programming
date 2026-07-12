#!/usr/bin/node

let biggest = -Infinity;
let secondBiggest = -Infinity;

for (let i = 2; i < process.argv.length; i++) {
  const current = parseInt(process.argv[i]);

  if (current > biggest) {
    secondBiggest = biggest;
    biggest = current;
  } else if (current > secondBiggest && current !== biggest) {
    secondBiggest = current;
  }
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondBiggest);
}

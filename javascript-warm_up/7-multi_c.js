#!/usr/bin/node

const mult = parseInt(process.argv[2]);

if (isNaN(mult)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < mult; i++) {
    console.log('C is fun');
  }
}

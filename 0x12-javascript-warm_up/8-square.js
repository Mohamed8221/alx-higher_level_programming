#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
    for (const i = 0; i < num; i++) {
        console.log ('X'.repeat(num));
    }
}
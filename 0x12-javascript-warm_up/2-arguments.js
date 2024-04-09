#!/usr/bin/node
const n = process.argv.length - 2;

if (n === 0) {
    console.log('No argument');
  } else if (n === 1) {
    console.log('Argument found');
  } else if (n > 1){
    console.log('Arguments found');
  }
  
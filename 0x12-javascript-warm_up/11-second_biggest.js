#!/usr/bin/node
if (process.argv.length <= 3) {
    console.log(0);
  } else {
    const nums = process.argv.slice(2).map(Number);
    const maxNum = Math.max(...nums);
    nums.splice(nums.indexOf(maxNum), 1);
    console.log(Math.max(...nums));
  }
  
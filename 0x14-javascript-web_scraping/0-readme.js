#!/usr/bin/node
// read file by argument and print the content of the file
const fs = require('fs');
fs.readFile('' + process.argv[2], 'utf8', (error, data) => {
  if (!error) {
    console.log(data);
  } else console.log(error);
});

#!/usr/bin/node
// write data in a file from argement and print the content of the file
const fs = require('fs');

if (process.argv.length > 3) {
  fs.writeFile(process.argv[2], process.argv[3], (error) => {
    if (error) console.log(error);
  });
}

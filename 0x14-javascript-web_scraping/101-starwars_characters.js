#!/usr/bin/node
// Get request
const request = require('request');
const movieId = process.argv[2];
if (!movieId) process.exit();

const moviesURL = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function makeRequest (url, charInMovie, index) {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < charInMovie.length) {
        makeRequest(charInMovie[index + 1], charInMovie, index + 1);
      }
    }
  });
}

request.get(moviesURL, (error, response, body) => {
  if (!error) {
    const charInMovie = JSON.parse(body).characters;
    makeRequest(charInMovie[0], charInMovie, 0);
  } else console.log(error);
});

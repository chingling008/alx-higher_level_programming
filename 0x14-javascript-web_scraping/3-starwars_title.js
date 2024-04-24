#!/usr/bin/node

const request = require('request');

const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info.title);
  }
}

request(options, callback);

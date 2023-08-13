#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  const requests = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
        } else if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          resolve(character.name);
        } else {
          reject(`Request failed with status
          code ${charResponse.statusCode}`);
        }
      });
    });
  });

  Promise.all(requests)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
    });
});


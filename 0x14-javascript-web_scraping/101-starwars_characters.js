#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Status:', response.statusCode);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  } catch (parseError) {
    console.error('Parse error:', parseError);
  }
});

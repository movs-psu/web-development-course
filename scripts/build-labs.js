//#!/usr/bin/node

const { buildInDir } = require('./utils');

buildInDir('./labs')
  .then(() => {
    console.log('Done');
  })
  .catch((e) => {
    console.log(e.message);
    console.error(e);
  });

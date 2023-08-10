#!/usr/bin/node

module.exports.nbOccurences = function (List, searchElement){
  return List.reduce((m, x) => x === searchElement ? m +1 : m, 0);
};

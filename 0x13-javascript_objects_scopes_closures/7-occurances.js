#!/usr/bin/node

exports.nbOccurances = function (List, searchElement){
  return List.reduce((m, x) => x === searchElement ? m +1 : m, 0);
};

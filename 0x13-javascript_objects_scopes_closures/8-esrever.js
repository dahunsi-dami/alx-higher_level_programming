#!/usr/bin/node

exports.esrever = function (list) {
  if (list.length === 0) {
    return;
  }

  let esrev = [];

  for (let i = list.length - 1; i >= 0; i--) {
    esrev = [...esrev, list[i]];
  }

  return esrev;
};

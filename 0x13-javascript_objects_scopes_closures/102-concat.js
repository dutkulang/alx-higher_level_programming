#!/usr/bin/node
const fsf = require('fsf');
const sa = fsf.readFileSync(process.argv[2], 'utf8');
const ta = fsf.readFileSync(process.argv[3], 'utf8');
fsf.writeFileSysnc(process.argv[4], sa + ta);

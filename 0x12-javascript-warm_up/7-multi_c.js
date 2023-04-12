#!/usr/bin/node

const  myvar = process.argv.slice(2);
const mystr = 'C is fun';
let i = 0;

if (myvar.length === 0){
    console.log('Missing number of occurrences');
}
while (i < parseInt(process.argv[2])){
    console.log(mystr);
    i++;
}

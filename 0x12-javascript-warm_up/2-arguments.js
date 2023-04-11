#!/usr/bin/node

const myVar = process.argv.slice(2);

if (myVar > 2){
	console.log('Argument found');
}
else{
	console.log('No argument');
}

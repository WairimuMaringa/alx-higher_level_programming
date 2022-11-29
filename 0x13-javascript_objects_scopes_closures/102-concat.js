#!/usr/bin/node
const fs = require('fs');

const fArg = fs.readFileSync(process.arg[2]).toString();
const sArg = fs.readFileSync(process.arg[3]).toString();
fs.writeFileSync(process.arg[4], fArg + sArg);

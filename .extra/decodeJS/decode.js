const GibberishAES = require('./node_modules/gibberish-aes/src/gibberish-aes');
const atob = require('atob');

//Decryption key
let key = "fee631d2cffda38a78b96ee6d2dfb43a";
let link_out = atob(process.argv[2]);
console.log(GibberishAES.dec(link_out, key));
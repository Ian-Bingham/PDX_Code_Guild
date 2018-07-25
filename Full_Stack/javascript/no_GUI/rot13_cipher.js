// rot13_cipher.js 7/24/18

alert("Hello. This is an encoder.");
alphabet = 'abcdefghijklmnopqrstuvwxyz';
let rotation_amt = prompt("How many encoding rotations would you like to do?\n> ")
let user_input = prompt("Please type in a word you would like to encode.\n> ")
user_input = user_input.toLowerCase();
let rotN = alphabet.slice(rotation_amt) + alphabet.slice(0, rotation_amt);
let encoded_str = '';

for(let i=0; i < user_input.length; i++) {
    if(alphabet.indexOf(user_input[i]) != -1) {
        let letter_position = alphabet.indexOf(user_input[i]);
        encoded_str += rotN[letter_position];
    }
    else {
        encoded_str += user_input[i];
    }
}

alert(`The encoded string is ${encoded_str}`);

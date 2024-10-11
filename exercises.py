function doubleInteger(i) {
  // i will be an integer. Double it and return it.
  return i * 2;
}

function smash (words) {
   return words.join(' ')
};


function sum(numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}


function greet(name){
  return `Hello, ${name} how are you doing today?`
}


function past(h, m, s){
  return (h*60*60*1000 + m*60*1000 + s*1000)
}

function findNeedle(haystack) {
  return "found the needle at position " + haystack.indexOf("needle");
}

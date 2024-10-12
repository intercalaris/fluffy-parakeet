function getCount(str) {
  const vowArr = ['a', 'e', 'i', 'o', 'u'];
  let vowCount = 0;
  for (i=0; i<5; i++) {
    for (j=0; j<str.length; j++) {
      str[j] === vowArr[i] ? vowCount++ : null;
    }
  }
  return vowCount;
}

function noSpace(x) {
  return x.replaceAll(' ', '');
}

function descendingOrder(n){
  return Number(n.toString().split('').sort((a,b) => (b-a)).join(''))
}

function makeNegative(num) {
  return num < 0 ? num : -num;
}

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

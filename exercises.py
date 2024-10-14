def string_to_number(s):
    return int(s)
    
class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const uniq_s = {};
        const uniq_t = {};
        for (let i = 0; i < s.length; i++) {
            if (s[i] in uniq_s) {
                uniq_s[s[i]] += 1;
            } else {
                uniq_s[s[i]] = 1;
            }
        }

        for (let i = 0; i < t.length; i++) {
            if (t[i] in uniq_t) {
                uniq_t[t[i]] += 1;
            } else {
                uniq_t[t[i]] = 1;
            } 
        }
        return Object.entries(uniq_t).sort().toString() === 
        Object.entries(uniq_s).sort().toString();
    }
}


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

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniq_s_dict = {}
        uniq_t_dict = {}
        for i in range(0, len(s)):
            if s[i] in uniq_s_dict:
                uniq_s_dict[s[i]] += 1
            else:
                uniq_s_dict[s[i]] = 1
        for i in range(0, len(t)):
            if t[i] in uniq_t_dict:
                uniq_t_dict[t[i]] += 1
            else:
                uniq_t_dict[t[i]] = 1
        return uniq_s_dict == uniq_t_dict


def digital_root(n):
    acc = 0
    if n < 10:
        return n
    else:
        for i in range(0, len(str(n))):
            acc += int(str(n)[i])
        return digital_root(acc)

function removeChar(str){
  str = str.split('').slice(1, str.length-1).join('');
  return str;
};

function isTriangle(a,b,c) {
  if (a + b > c && a + c > b && b + c > a && c + b > a ) {
    return true;
  } else {
    return false;
    }
}

var isSquare = function(n){
  return Number.isInteger(Math.sqrt(n)); 
}
function booleanToString(b){
  return b.toString()
}

function maps(x){
  return x.map((el) => el *2)
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

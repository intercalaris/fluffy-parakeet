function nbYear(p0, percent, aug, p) {
  let years = 0;
  for (let currPop = p0; currPop < p; currPop += Math.floor(currPop * percent/100) + aug) {
    years++;
  } 
  return years;
}

import math
def nb_year(p0, percent, aug, p):
    years = 0;
    curr_pop = p0;
    while curr_pop < p:
        curr_pop += math.floor(curr_pop * percent/100) + aug
        years += 1
    return years


function dnaStrand(dna){
  let dnaArr = dna.split('');
  for (let i = 0; i < dnaArr.length; i++) {
    if (dnaArr[i] === 'A') {
      dnaArr[i] = 'T';
    }
    else if (dnaArr[i] === 'T') {
      dnaArr[i] = 'A';
    }
    else if (dnaArr[i] === 'G') {
      dnaArr[i] = 'C';
    }
    else if (dnaArr[i] === 'C') {
      dnaArr[i] = 'G';
    }
  }
  return dnaArr.join('');
}

def lovefunc( flower1, flower2 ):
    return (flower1 % 2 == 0 and flower2 % 2 != 0 or flower2 % 2 == 0 and flower1 % 2 != 0) 
function lovefunc(flower1, flower2){
    return (flower1 % 2 === 0 && flower2 % 2 !== 0 || flower2 % 2 === 0 && flower1 % 2 !== 0) 
}

def solution(number):
    if number < 0:
        return 0

  
    sum = 0
    for i in range(0, number, 1):
        if i % 3 == 0 or i % 5 == 0:
            sum+= i;
    return sum

def reverseWords(str):
    k = str.split(' ')
    k.reverse()
    str = ' '.join(k)
    return str
    
function reverseWords(str){
  return str.split(' ').reverse().join(' '); // reverse those words
}
function solution(number) {
  if (number < 0) return 0;

  let sum = 0;
  
  for (let i = 0; i < number; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      sum += i;
    }
  }

  return sum;
}


def string_to_number(s):
    return int(s)
function isPangram(string){ 
  const alph = 'abcdefghijklmnopqrstuvwxyz';
  string = string.toLowerCase();
  for (let i = 0; i < alph.length; i++) {
    if (!string.includes(alph[i])) {
      return false;
    }
  }
  return true;
}

def is_pangram(st):
    if len(''.join((st).split(' '))) < 26:
        return False
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for char in range(0, len(alph)):
        if alph[char] not in st.lower():
            return False
    return True
 
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
def neutralise(s1, s2):
    str = ''
    for i in range(len(s1)):
        if s1[i] == '+' and s2[i] == '+':
            str = str + '+'
        elif s1[i] == '+' and s2[i] == '-' or s2[i] == '+' and s1[i] == '-':
            str = str + '0'
        elif s1[i] == '-' and s2[i] == '-':
            str = str + '-'
    return str
function neutralise(s1, s2) {
    let  str = ''
    for (let i = 0; i < s1.length; i++) {
              if (s1[i] == '+' && s2[i] == '+') {
            str = str + '+';
        }
        else if (s1[i] == '+' && s2[i] == '-' || s2[i] == '+' && s1[i] == '-') {
          str = str + '0';
        }
            
        else if (s1[i] == '-' && s2[i] == '-'){
          str = str + '-';
        }
    }
      
    return str;
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

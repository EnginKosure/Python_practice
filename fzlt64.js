const x = (st, l) => [...st].filter(i => i == l).length
const y = (st, l) => [...st].reduce((a, c) => c == l ? ++a : a, 0)

const z = (st, l) => [...st].map((i, index, arr) => i == l ? i : null)

console.log(x('claruswayaa', 'a'))
console.log(y('claruswayaa', 'a'))
console.log(z('claruswayaa', 'a'))

var temp = "This is a string.";
var count = (temp, l) => (temp.match(/i/g) || []).length;
console.log(count(temp, 'i'));

// Output: 2

// Explaination : The g in the regular expression (short for global) says to search 
// the whole string rather than just find the first occurrence. 
// This matches 'is' twice.
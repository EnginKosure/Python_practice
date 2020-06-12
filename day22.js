const isRepdigit = num => new Set('' + num).size === 1;
console.log(isRepdigit(7777));//true
console.log(isRepdigit(33));//true
console.log(isRepdigit(678));//false

let mySet = new Set()

mySet.add(1)           // Set [ 1 ]
mySet.add(5)           // Set [ 1, 5 ]
mySet.add(5)           // Set [ 1, 5 ]
mySet.add('some text') // Set [ 1, 5, 'some text' ]
let o = { a: 1, b: 2 }
mySet.add(o)

mySet.add({ a: 1, b: 2 })   // o is referencing a different object, so this is okay

mySet.has(1)              // true
mySet.has(3)              // false, since 3 has not been added to the set
mySet.has(5)              // true
mySet.has(Math.sqrt(25))  // true
mySet.has('Some Text'.toLowerCase()) // true
mySet.has(o)       // true
//size for Set is the same of length for string or array
mySet.size         // 5

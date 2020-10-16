// Write a code that give us number of items in an array.
myArray = ["clarusway", "google", "adobe", "cisco", 'space - x', "clarusway", "cisco", "clarusway", "facebook", "google", "clarusway"]
// Output:
// { clarusway: 4, google: 2, adobe: 1, cisco: 2, spaceX: 1, facebook: 1 }

const c = a => a.reduce((a, c) => (a[c] = ++a[c] || 1, a), {});
// console.log(c(myArray))

// let newArray = arr.map(callback(currentValue[, index[, array]]) {
//     // return element for newArray, after executing something
// }[, thisArg]);

let names = ['Alice', 'Bob', 'Tiff', 'Bruce', 'Alice']

let countedNames = names.reduce(function (allNames, name) {
    if (name in allNames) {
        allNames[name]++
    }
    else {
        allNames[name] = 1
    }
    return allNames
}, {})
// countedNames is:
// { 'Alice': 2, 'Bob': 1, 'Tiff': 1, 'Bruce': 1 }
// let names = ['Alice', 'Bob', 'Tiff', 'Bruce', 'Alice']
let countedNames1 = (x) => x.reduce((acc, curr) => (acc[curr] = ++acc[curr] || 1, acc), {})

console.log(countedNames1(names))



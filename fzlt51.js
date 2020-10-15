// Write a code that give us number of items in an array.
myArray = ["clarusway", "google", "adobe", "cisco", 'space - x', "clarusway", "cisco", "clarusway", "facebook", "google", "clarusway"]
// Output:
// { clarusway: 4, google: 2, adobe: 1, cisco: 2, spaceX: 1, facebook: 1 }

const c = a => a.reduce((p, c) => (p[c] = ++p[c] || 1, p), {});
console.log(c(myArray))

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
//1-->acc {}                   ## curr 'Alice' -->{'Alice':1}
//2-->acc {'Alice':1}         ## curr 'Bob'    -->{'Alice':1, 'Bob':1}
//3-->acc {'Alice':1, 'Bob':1}## curr 'Tiff'    -->


// var myArray = ["goog", 'aai', "adobe", "cisco", "cisco", "face", "google", "clar"];
var myArray = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6];
var a;
var sum = 0;
// myArray.sort();
console.log(myArray);
const asdf = (ar) => {
    for (a of ar) {
        while (ar.includes(a)) {
            sum++;
            ar.shift();
        }
        console.log('qqq', a, ar)
        console.log(a, ':', sum);
        sum = 0;
    }
}
console.log(asdf(myArray));

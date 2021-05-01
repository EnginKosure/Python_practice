const _ = require('lodash')
const add = (a, b) => a + b
const curriedAdd = a => b => add(a, b)

const addTwo = curriedAdd(6)

addTwo(2) // 8
addTwo(4) // 10
console.log(addTwo(4));//10

function curry(f) { // curry(f) does the currying transform
    return function (a) {
        return function (b) {
            return f(a, b);
        };
    };
}

// usage
function sum(a, b) {
    return a + b;
}

let curriedSum = curry(sum);

console.log(curriedSum(1)(2)); // 3

function log(date, importance, message) {
    console.log(`[${date.getHours()}:${date.getMinutes()}] [${importance}] ${message}`);
}
log = _.curry(log);
log(new Date(), "DEBUG", "some debug"); // log(a, b, c)
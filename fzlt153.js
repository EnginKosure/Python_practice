
const add = (a, b) => a + b
const curriedAdd = a => b => add(a, b)

const addTwo = curriedAdd(2)

addTwo(2) // 4
addTwo(4) // 6
console.log(addTwo(4));
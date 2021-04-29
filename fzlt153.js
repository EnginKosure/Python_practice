
const add = (a, b) => a + b
const curriedAdd = a => b => add(a, b)

const addTwo = curriedAdd(6)

addTwo(2) // 8
addTwo(4) // 10
console.log(addTwo(4));//10
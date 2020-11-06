const x = (st, l) => [...st].filter(i => i == l).length
const y = (st, l) => [...st].reduce((a, c) => c == l ? ++a : a, 0)


console.log(x('claruswayaa', 'a'))
console.log(y('claruswayaa', 'a'))
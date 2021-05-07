console.time('timer')

const items = []
for (let i = 0; i < 1000000; i++) {
    items.push(i)
}

console.timeEnd('timer')
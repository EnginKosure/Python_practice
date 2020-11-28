/* 1) Çarpma işareti olmadan çarpma işlemi yapan bir fonksiyon yazın: 
    * sumWithoutMultiply(3, 5)
Output: 15 
2) Verilen parayı note olarak hesaplayan, terminale ona göre çıktı yazan dongüsel bir fonksiyon yazın.
    * calculateMoney(501)
Output: 
    Current money is 501: 2 x 200
    Current money is 101: 1 x 100
    Current money is 1: 1 x 1
 (note için array: [200, 100, 50, 20, 10, 5, 1])*/

function sumWithoutMultiply(x, y) {
    let sum = 0;
    for (let i = 0; i < x; i++) {
        sum += y;
    }
    return sum;
}

console.log(sumWithoutMultiply(3, 5))

function calculateMoney(money) {
    let result = ''
    const note = [200, 100, 50, 20, 10, 5, 1]
    for (let i = 0; i < note.length; i++) {
        if (money >= note[i]) {
            let divFirst = Math.floor(money / note[i])
            result += `Current money is ${money}: ${divFirst} x ${note[i]}\n`
            money = money % note[i];
        }
    }
    return (result)
}
console.log(calculateMoney(7121))

console.log(process.env.VAR)
const EventEmitter = require('events')
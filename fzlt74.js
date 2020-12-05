function binaryToDecimal(binaryNumber) {
    let total = 0;
    for (let i = 0; i < binaryNumber.length; i++) {
        var bit = binaryNumber.charAt(binaryNumber.length - (i + 1));
        if (bit == 1) {
            let temp = Math.pow(2, i * parseInt(bit));
            total += temp;
        }
    }
    return total;
}
// console.log(binaryToDecimal("1111"))

// function binary_to_decimal(bstring) {
//     console.log(bstring.slice(-1));
//     if (bstring.length == 0) {
//         return 0
//     }
//     return binary_to_decimal(bstring.slice(0, -1)) * 2 + (bstring.slice(-1) == '1')
// }

const b_t_d = bs => bs.length == 0 ? 0 : b_t_d(bs.slice(0, -1)) * 2 + (bs.slice(-1) == '1');
console.log(b_t_d("11"))
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
console.log(binaryToDecimal("1111"))
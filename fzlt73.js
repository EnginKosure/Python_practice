const number = 12;
function convertDecimalToBinary(number) {
    let binary = "";
    while (number > 0) {
        if (number % 2 == 0) {
            binary = "0" + binary;
            console.log('binary-2yebolunuyorsa', binary);
        }
        else {
            binary = "1" + binary;
            console.log('binary-2yebolunmuyorsa', binary);

        }
        number = Math.floor(number / 2);
    }
    return binary;
}
console.log(convertDecimalToBinary(number));//1001000
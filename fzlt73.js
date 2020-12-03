const number = 12;
function convertDecimalToBinary(number) {
    var binary = "";
    var temp = number;
    while (temp > 0) {
        if (temp % 2 == 0) {
            binary = "0" + binary;
            console.log('binary-2yebolunuyorsa', binary);
        }
        else {
            binary = "1" + binary;
            console.log('binary-2yebolunmuyorsa', binary);

        }
        temp = Math.floor(temp / 2);
    }
    return binary;
}
console.log(convertDecimalToBinary(number));//1001000
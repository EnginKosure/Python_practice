/* Write a function that:
- takes an array of numbers as input
- returns an array of strings formatted as percentages (e.g. 10 => "10%")
- the numbers must be rounded to 2 decimal places
- numbers greater 100 must be replaced with 100
*/


function formatPercentage(arr) {
    console.log(arr.toString());

    let newFormatted = [];
    let formatStringNumbers = arr.map(x => Math.round((x + Number.EPSILON) * 100) / 100).toString().split(",");
    for (let i = 0; i < formatStringNumbers.length; i++) {
        if (formatStringNumbers[i] > 100) {
            newFormatted.push('100%')
        } else {
            newFormatted.push(formatStringNumbers[i] + '%');
        }
    }
    return newFormatted;
}
console.log(formatPercentage([2, 50, 102, 30, 2.4567, 1.005])); //[ '2%', '50%', '100%', '30%' ]
console.log(formatPercentage([2, 50, 102, 30, 67.0034]));

function formatPercentage1(arr) {

    for (let i = 0; i < arr.length; i++) {

        if (arr[i] > 100) {
            arr[i] = 100;
        } else {
            arr[i] = Math.round(arr[i] * 100) / 100;
        }
        arr[i] += "%";
    }
    return arr;
}
console.log(formatPercentage1([2, 50, 102, 30, 67.0034]));
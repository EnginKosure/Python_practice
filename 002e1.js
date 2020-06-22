/* Write a function that:
- takes an array of numbers as input
- returns an array of strings formatted as percentages (e.g. 10 => "10%")
- the numbers must be rounded to 2 decimal places
- numbers greater 100 must be replaced with 100
*/


function formatPercentage(arr) {
    console.log(arr.toString().split(','));

    let newFormatted = [];
    // let formatStringNumbers = parseFloat(arr.toString().split(",")).toFixed(2);
    // console.log(formatStringNumbers);

    // for (let i = 0; i < formatStringNumbers.length; i++) {
    //     if (formatStringNumbers[i] > 100) {
    //         formatStringNumbers[i] = formatStringNumbers[100];
    //     } else {
    //         newFormatted = formatStringNumber.push(newFormatted);
    //         return newFormatted;
    //         console.log(newFormatted);
    //     }
    // }
    console.log(newFormatted);
}
console.log(formatPercentage([2, 50, 102, 30]));
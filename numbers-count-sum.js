/* Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]. */

function countPositivesSumNegatives(input) {

    let solutionArray = [];
    let positiveCount = 0;
    let negativeSum = 0;
    if (input === null || input.length === 0)
        return [];
    let arrayWithoutZero = input.filter(x => x !== 0);

    // console.log(arrayWithoutZero);

    for (let i = 0; i < arrayWithoutZero.length; i++) {

        if (arrayWithoutZero[i] > 0) {
            positiveCount++;
        }
        if (arrayWithoutZero[i] < 0) {
            negativeSum += arrayWithoutZero[i];
        }

    }
    solutionArray.push(positiveCount);
    solutionArray.push(negativeSum);
    // console.log(solutionArray);
    return solutionArray;
}
let exem = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, 0, -14, -15];
console.log(countPositivesSumNegatives(exem));
console.log(countPositivesSumNegatives([]));
console.log(countPositivesSumNegatives(null));
console.log(countPositivesSumNegatives([null]));



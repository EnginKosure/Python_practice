const array = [5, 1, 22, 25, 6, -1, 8, 10];
const sequence = [1, 6, -1, -1, 10]

function isValidSubsequence(array, sequence) {
    // Write your code here.
    return sequence.every(r => array.includes(r))

}

console.log(isValidSubsequence(array, sequence))
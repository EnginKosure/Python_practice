
function sortAges(arr) {
    let done = false;
    while (!done) {
        done = true;
        for (let i = 0; i < arr.length; i++) {
            if (typeof arr[i] !== "number") {
                //removes one element from the index i and 
                // to check the next number, decreases the index --
                arr.splice(i, 1); i--;
            }
            if (arr[i] > arr[i + 1]) {
                done = false;
                // let tmp = arr[i];
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
                // arr[i + 1] = tmp;
            }
        }
    }
    console.log(arr);
    return arr;
}

// sortAges(['something', 55, 0, 3, 2, 13, 4, '23', 'integer', 1, 7, 3])//[ 0, 1, 2, 3, 3, 4, 7, 13, 55 ]

function sortAges1(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (typeof arr[i] !== "number") {
            //removes one element from the index i and 
            // to check the next number, decreases the index --
            arr.splice(i, 1); i--;
        }
    }

    if (arr.length <= 1) {
        return arr;
    }

    var pivot = arr[0];

    var left = [];
    var right = [];

    for (var i = 1; i < arr.length; i++) {
        arr[i] < pivot ? left.push(arr[i]) : right.push(arr[i]);
    }
    return sortAges1(left).concat(pivot, sortAges1(right));
};

var unsorted = [23, 45, 16, 37, 3, 99, 22];
var sorted = sortAges1(unsorted);

console.log('Sorted array', sorted);

const a = sortAges1(['something', 55, 0, 3, 2, 13, 4, '23', 'integer', 1, 7, 3])//[ 0, 1, 2, 3, 3, 4, 7, 13, 55 ]
console.log(a);

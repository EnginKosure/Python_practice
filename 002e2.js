// function sortAges(arr) {
//     let maximum = 0;
//     for (let i = 0; i < arr.length; i++) {
//         if (typeof arr[i] !== "number") {
//             //removes one element from the index i and 
//             // to check the next number, decreases the index --
//             arr.splice(i, 1); i--;
//         }
//         for (let i = 0; i < arr.length; i++) {
//             if (arr[i] > arr[i + 1]) {
//                 let tmp = arr[i];
//                 arr[i] = arr[i + 1];
//                 arr[i + 1] = tmp;
//             }
//         }
//     }
//     console.log(arr);
//     return arr;
// }

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

sortAges(['something', 55, 0, 3, 2, 13, 4, '23', 'integer', 1, 7, 3])//[ 0, 1, 2, 3, 3, 4, 7, 13, 55 ]

// var arr = [1, 2, 3, 4, 5, 5, 6, 7, 8, 5, 9, 0];
// for (var i = 0; i < arr.length; i++) {
//     if (arr[i] === 5) {
//         arr.splice(i, 1); i--;
//     }
// }//=> [1, 2, 3, 4, 6, 7, 8, 9, 0]
function bubbleSort(array) {
    let done = false;
    while (!done) {
        done = true;
        for (var i = 1; i < array.length; i++) {
            if (array[i - 1] > array[i]) {
                done = false;
                let tmp = array[i - 1];
                array[i - 1] = array[i];
                array[i] = tmp;
            }
        }
    }

    return array;
}

var numbers = [12, 10, 15, 11, 14, 13, 16];
bubbleSort(numbers);
console.log(numbers);
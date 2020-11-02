function solve(a) {
    let newArray = a.filter(e => typeof (e) === "number");
    console.log(newArray);
    let evenArr = [];
    let oddArr = [];
    newArray.forEach(n => {
        if (n % 2 === 0) {
            evenArr.push(n);
        } else if (n % 2 !== 0) {
            oddArr.push(n);
        } else {
            null
        }
    })

    let evenN = evenArr.length
    console.log(evenN);
    let oddN = oddArr.length
    console.log(oddN);
    let result = ((evenN) - (oddN));
    return result;

    console.log(evenN);
};

console.log(solve([5, 15, 16, 10, 6, 4, 16, 't', 13, 'n', 14, 'k', 'n', 0, 'q', 'd', 7, 9]), 2);
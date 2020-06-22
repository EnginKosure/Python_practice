/*
Write a function that:
- takes an array of strings as input
- removes any spaces in the beginning or end of the strings
- removes any forward slashes (/) in the strings
- makes the string all lowercase
*/


function tidyUpString(strArr) {
    let makeTidyUpArray = [];
    let a = '';
    for (let i = 0; i < strArr.length; i++) {
        a = strArr[i].trim().replace('/', '').toLowerCase();
        makeTidyUpArray.push(a);
    }
    console.log(makeTidyUpArray); // [ 'daniel', 'irina', 'gordon', 'ashleigh' ]
    const c = makeTidyUpArray.join(', ')
    console.log(c); //daniel, irina, gordon, ashleigh

    return makeTidyUpArray;
}
tidyUpString(["/Daniel ", "irina ", " Gordon", "ashleigh "]);
//Extending buit-in functions are considered bad-practice.
//Because it makes the buit-in function heavier and if any name conflict appears, it will crash.
//For a better way, see fzlt140.js

//Custom average function
Array.prototype.average = function () {
    return this.reduce((acc, elem) => acc + elem) / this.length;
}
const list = [1, 2, 3, 4, 5]
const avg = list.average();
console.log(avg);
//Custom average function
Array.prototype.average = function () {
    return this.reduce((acc, elem) => acc + elem) / this.length;
}
const list = [1, 2, 3, 4, 5]
const avg = list.average();
console.log(avg);
class ArrayUtils {
    //Custom average function
    static average(list) {
        return list.reduce((acc, elem) => acc + elem) / list.length;
    }
}
const list = [1, 2, 3, 4, 5]
const avg = ArrayUtils.average(list);
console.log(avg);
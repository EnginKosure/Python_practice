// Perfect Number: In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors,
// excluding the number itself. For instance, 6 has divisors 1, 2 and 3, and 1 + 2 + 3 = 6,so 6 is a perfect number.

const perfectNumber = (num) => {
    let result = 0;
    for (i = 0; i < num; i++) {
        if (num % i == 0) {
            result += i

        }
    }
    result == num ? console.log('It is a perfect number') : console.log('It is not a perfect number');
}
perfectNumber(12)
/*First, let's create a function that creates a list of all the frequencies.
 * Call this function `getAllFrequencies`.
 * This function should:
 * - Create an array  starting at 87 and ending in 108
 * - Should return this array to use in other functions
 */

// `getAllFrequencies` goes here    
function getAllFrequencies() {
    let allFrequencies = [];
    for (let i = 87; i < 108; i++) {
        allFrequencies.push(i);
    }
    console.log(allFrequencies);

    return allFrequencies;
}
getAllFrequencies();
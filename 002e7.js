function aliasGen(first, lastName) {
    let firstNameLetterFirst = first[0].toUpperCase();
    let lastNameLetterFirst = lastName[0].toUpperCase();
    console.log(firstName[firstNameLetterFirst]);
    const upperCasedAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    if (!upperCasedAlphabet.includes(firstNameLetterFirst) || !upperCasedAlphabet.includes(lastNameLetterFirst)) {
        return "Your name must start with a letter from A - Z.";
    } else {
        return firstName[firstNameLetterFirst] + ' ' + surname[lastNameLetterFirst];
    }
}

var firstName = { A: 'Alpha', B: 'Beta', C: 'Cache' }
var surname = { A: 'Analogue', B: 'Bomb', C: 'Catalyst' }

console.log(aliasGen('Aarry', 'Brentwood'));

// aliasGen('123abc', 'Petrovic') === 'Your name must start with a letter from A - Z.'
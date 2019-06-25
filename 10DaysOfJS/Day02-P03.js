function vowelsAndConsonants(s) {

    let vowels = ['a', 'e', 'i', 'o', 'u']

    for (let char of s) {
        if (vowels.includes(char)) {
            console.log(char)
        }
    }
    for (let char of s) {
        if (!vowels.includes(char)) {
            console.log(char)
        }
    }
}

const fs = require("fs");
const [a, b] = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n\n");
let c = a.split("\n")
let ranges = c.map(line => line.split("-").map(Number));
let ingredients =b.split("\n").map(Number)
let total = 0
for (let i = 0; i < ingredients.length; i++) {
    let frash = false
    for (let j = 0; j < ranges.length; j++) {
        if ( ingredients[i] >= ranges[j][0] && ingredients[i] <= ranges[j][1] ) {
            frash = true
        }
    }
    if (frash) {
        total += 1
    }
}
console.log(total)
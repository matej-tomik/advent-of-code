const fs = require("fs");
const [a, b,c,d,e] = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n");
let first = a.split(/\s+/).map(Number)
let second = b.split(/\s+/).map(Number)
let thrd = c.split(/\s+/).map(Number)
let forth = d.split(/\s+/).map(Number)
let symbol = e.split(/\s+/)
let total = 0

for (let i = 0; i < first.length; i++) {
    if (symbol[i] === "*") {
        total += (first[i] * second[i] * thrd[i] * forth[i])
    }
    if (symbol[i] === "+") {
        total += (first[i] + second[i] + thrd[i]  +  forth[i])
    }
}

console.log(total)
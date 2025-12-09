const fs = require("fs");
const [a, b,c,d,e] = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n");
let first = a.match(/\d+\s*/g).map(x => x.replace(/\s$/, ""))
let second = b.match(/\d+\s*/g).map(x => x.replace(/\s$/, ""))
let thrd = c.match(/\d+\s*/g).map(x => x.replace(/\s$/, ""))
let forth = d.match(/\d+\s*/g).map(x => x.replace(/\s$/, ""))
let symbol = e.split(/\s+/)
let total = 0

for (let i = 0; i < first.length; i++) {
     console.log([first[i], second[i], thrd[i], forth[i]])
    let temp = []
    for (let j = first[i].length - 1; j >= 0; j--) {
        temp.push(Number((first[i][j] + second[i][j] + thrd[i][j] + forth[i][j]).replace(/\s+/g, "")))
    }
    if (symbol[i] === "*") {
        console.log(temp)
        total += temp.reduce((acc, x) => acc * x, 1);
    }
    if (symbol[i] === "+") {
        console.log(temp)
        total += temp.reduce((acc, x) => acc + x, 0);
    }
}

console.log(total)


//nedokonceno - problemy s parsovanim
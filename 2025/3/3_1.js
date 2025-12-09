const fs = require("fs");
let total = 0
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n");
for (let i = 0; i < data.length; i++) {
    let biggest = null
    for (let j = 0; j < data[i].length - 1; j++) {
        for (let k = j+1; k < data[i].length; k++) {
            let current = Number(data[i][j]+data[i][k])
            if (biggest <  current)
            biggest = current
        }
    }
    total += biggest
}
console.log("result:");
console.log(total);
const fs = require("fs");
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n");
let rows = data.length
let coloms = data[0].length
let start_colom = null
let total = 0

for (let i = 0; i < coloms; i++) {
    if (data[0][i]==="S") {
        start_colom = i
        break
    }
}

let Q = [[0, start_colom]];
let SEEN = new Set();

while (Q.length > 0) {
    let [r, c] = Q.shift();
    let key = `${r},${c}`;
    if (SEEN.has(key)) continue

    SEEN.add(key);
    if (r + 1 === rows) continue

    if (data[r + 1][c] === '^') {
        Q.push([r + 1, c - 1]);
        Q.push([r + 1, c + 1]);
        total += 1;
    } else {
        Q.push([r + 1, c]);
    }
}

console.log(total)
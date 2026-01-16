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

const cache = new Map();

function score(r, c) {
    const key = `${r},${c}`;

    if (cache.has(key)) {
        return cache.get(key);
    }

    let result;

    if (r + 1 === rows) {
        result = 1;
    } else if (data[r + 1][c] === '^') {
        result = score(r + 1, c - 1) + score(r + 1, c + 1);
    } else {
        result = score(r + 1, c);
    }

    cache.set(key, result);
    return result;
}

console.log(score(0, start_colom))
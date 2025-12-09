const fs = require("fs");
const [a, b] = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n\n");
let c = a.split("\n")
let ranges = c.map(line => line.split("-").map(Number));
ranges.sort((a, b) => a[0] - b[0]);
let merged = [];
let current = ranges[0];

for (let i = 1; i < ranges.length; i++) {
    let [start, end] = ranges[i];

    if (start <= current[1]) {
        current[1] = Math.max(current[1], end);
    } else {
        merged.push(current);
        current = ranges[i];
    }
}
merged.push(current);

let total = merged.reduce((sum, [start, end]) => sum + (end - start + 1), 0);
console.log(total)
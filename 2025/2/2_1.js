const fs = require("fs");
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split(",");

function invalid(numStr) {
    if (numStr.length % 2 !== 0) return false;  
    const half = numStr.length / 2;
    return numStr.slice(0, half) === numStr.slice(half);
}

let total = 0;

for (let i = 0; i < data.length; i++) {
    const [start, end] = data[i].split("-");
    for (let i = Number(start); i <= Number(end); i++) {
        if(invalid(i.toString())) {
            total += i;
        }
    }
}

console.log(total);

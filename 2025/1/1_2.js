const fs = require("fs");
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n");
let startingPoint = 50;
let total = 0;

for (let i = 0; i < data.length; i++) {
    const dir = data[i][0]; 
    const dist = Number(data[i].slice(1));
    for (let j= 0; j < dist; j++) {
        if (dir === "R") {
            startingPoint = (1 + startingPoint ) % 100 ;
        }else {
            startingPoint = (startingPoint - 1 + 100) % 100;
        }
        if (startingPoint === 0) {
            total += 1;
        }
    }
}

console.log(total);
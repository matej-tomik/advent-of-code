const fs = require("fs");
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n").map(line => line.split(","));
let total = 0;
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data.length; j++) {
        const area = Math.abs(data[i][0] - data[j][0] + 1) * Math.abs(data[i][1] - data[j][1] + 1);
        if (area > total){
            total = area
        }
    }
}
console.log(total)
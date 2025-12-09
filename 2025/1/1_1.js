const fs = require("fs");
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n");

function circularAccess(index, strartingPoint) {
    if (index[0] === "R") {
        return (Number(index.slice(1)) + strartingPoint ) % 100 ;
    }
    if (index[0] === "L")   
    return ((Number(index.slice(1)) + strartingPoint ) % 100 + 100) % 100;
}
let startingPoint = 50;
let total = 0;

for (let i = 0; i < data.length; i++) {
   startingPoint = circularAccess( data[i], startingPoint); 
    if (startingPoint === 0) { 
        total += 1;
    }
}

console.log(total);
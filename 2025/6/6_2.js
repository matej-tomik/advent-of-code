const fs = require("fs");
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n");

function splitByEmptyColumns(lines) {
    const width = lines[0].length;
    const height = lines.length;
    let problems = [];
    let startCol = null;

    for (let col = 0; col < width; col++) {
        let isEmpty = true;
        for (let row = 0; row < height; row++) {
            if (lines[row][col] !== " ") {
                isEmpty = false;
                break;
            }
        }

        if (!isEmpty && startCol === null) {
            startCol = col;
        }

        if ((isEmpty || col === width - 1) && startCol !== null) {
            const endCol = isEmpty ? col : col + 1;
            const problem = lines.map(line => line.slice(startCol, endCol));
            problems.push(problem);
            startCol = null;
        }
    }

    return problems;
}



let total = 0;
let problems = splitByEmptyColumns(data);
for (let i = 0; i < problems.length; i++) {
    let numbers = problems[i].slice(0, -1);
    let maxLen = Math.max(...numbers.map(n => n.length));
    let result = [];

    for (let col = maxLen - 1; col >= 0; col--) { 
        let num = "";
        for (let row = 0; row < numbers.length; row++) {
            if (numbers[row][col] !== " ") num += numbers[row][col];
        }
        if (num) result.push(Number(num)); 
    }
    if (problems[i][4].trim() === "*") {
        total += result.reduce((acc, x) => acc * x, 1);
    } else if (problems[i][4].trim() === "+") {
        total += result.reduce((acc, x) => acc + x, 0);
    }
}
console.log(total);

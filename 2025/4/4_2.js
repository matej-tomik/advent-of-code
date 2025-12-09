const { channel } = require("diagnostics_channel");
const fs = require("fs");
let data = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n");
let rows = data.length
let coloms = data.length
let total = 0
let change = true
while (true) {
    change = false
    let next = data.map(row => [...row]);
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < coloms; j++) {
            let count = 0
            for (let k = -1; k <= 1; k++) {
                for (let l = -1; l <= 1; l++) {
                    let row = i + k
                    let colom = j + l
                    if (row >= 0 && row < rows && colom >= 0 && colom < coloms){
                        if (data[row][colom] === "@") {
                            count +=1
                        }
                    }
                } 
            }
            if (count < 5 && data[i][j] === "@") {
                change = true
                total += 1
                next[i][j] = "."
            }
        }
    }
    if (!change) {
        break
    }
    data = next;
}
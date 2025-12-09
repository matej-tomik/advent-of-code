const fs = require("fs");
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split(",");

function invalid(numStr) {
    for (let k = 2; k <= (numStr.length); k++) {
        if (numStr.length % k == 0) {
            let cerrect = true
            let size = Math.trunc(numStr.length / k)
            let i = 0;
            while (i < numStr.length) {
                if (numStr.slice(i, i + size) !== numStr.slice(0, size)) {
                    cerrect = false
                }
                i += size;  
            }
            if (cerrect) {
                return true
            }
        }
    }
    return false;
}

let total = 0;

for (let i = 0; i < data.length; i++) {
    const [start, end] = data[i].split("-");
    for (let j = Number(start); j <= Number(end); j++) {
        if(invalid(j.toString())) {
            total += j;
        }
    }
}

console.log(total);
const fs = require("fs");
let total = 0
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n");

function F(line) {
  const n = line.length;
  const maxUsed = 12;

  const DP = Array.from({ length: n + 1 }, () => Array(maxUsed + 1).fill(undefined));

  function dfs(i, used) {
    if (i === n && used === maxUsed) return 0;
    if (i === n) return -1e20;

    if (DP[i][used] !== undefined) return DP[i][used];

    let ans = dfs(i + 1, used);

    if (used < maxUsed) {
      const digit = Number(line[i]);
      ans = Math.max(ans, Math.pow(10, 11 - used) * digit + dfs(i + 1, used + 1));
    }

    DP[i][used] = ans;
    return ans;
  }

  return dfs(0, 0);
}

for (let i = 0; i < data.length; i++) {
    const line = data[i];
    total += F(line);
}
console.log("result:");
console.log(total);
const fs = require("fs");
const data = fs.readFileSync("puzzle_imput.txt", "utf8").split("\n").map(line => line.split(","));
const D = [];

for (let i = 0; i < data.length; i++) {
  const [x1, y1, z1] = data[i];

  for (let j = 0; j < i; j++) {
    const [x2, y2, z2] = data[j];
    const distance = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2;

    D.push([distance, i, j]);
  }
}

D.sort((a, b) => a[0] - b[0]);
const UF = Array.from({ length: data.length }, (_, i) => i);

function find(x) {
  if (UF[x] !== x) {
    UF[x] = find(UF[x]);
  }
  return UF[x];
}

function mix(x, y) {
  UF[find(x)] = find(y);
}

let connections = 0;

for (let t = 0; t < D.length; t++) {
  const [_d, i, j] = D[t];

  if (t === 1000) {
    const SZ = new Map();

    for (let x = 0; x < data.length; x++) {
      const root = find(x);
      SZ.set(root, (SZ.get(root) || 0) + 1);
    }

    const S = Array.from(SZ.values()).sort((a, b) => a - b);
    console.log(S[S.length - 1] * S[S.length - 2] * S[S.length - 3]);
  }

  if (find(i) !== find(j)) {
    connections++;

    if (connections === data.length - 1) {
      console.log(data[i][0] * data[j][0]);
    }

    mix(i, j);
  }
}
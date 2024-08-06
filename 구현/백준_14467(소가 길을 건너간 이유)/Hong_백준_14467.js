const fs = require("fs");

const input = fs.readFileSync("input.txt").toString().trim().split("\n");

const n = parseInt(input[0]);

const data = input.slice(1).map((line) => line.split(" ").map(Number));

function solution(n, data) {
  let crossTheRoad = 0;
  data.sort((a, b) => a[0] - b[0]);
  for (i = 0; i < data.length - 1; i++) {
    if (data[i][0] === data[i + 1][0] && data[i][1] !== data[i + 1][1]) {
      crossTheRoad = crossTheRoad + 1;
    }
  }
  return crossTheRoad;
}

console.log(solution(n, data));

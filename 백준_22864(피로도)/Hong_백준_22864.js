const fs = require("fs");

const input = fs.readFileSync("input.txt").toString().trim().split(" ");

const A = parseInt(input[0]);
const B = parseInt(input[1]);
const C = parseInt(input[2]);
const M = parseInt(input[3]);

function solution(A, B, C, M) {
  let tired = 0;
  let totalWork = 0;
  for (let i = 1; i <= 24; i++) {
    if (tired + A <= M) {
      totalWork = totalWork + B;
      tired = tired + A;
      console.log("total", totalWork);
      console.log("tired", tired);
    } else {
      tired = tired - C;
      if (tired < 0) {
        tired = 0;
      }
    }
  }
  console.log("tired", tired);
  console.log("total", totalWork);

  if (M < tired) {
    return 0;
  } else {
    return totalWork;
  }
}

console.log(solution(A, B, C, M));

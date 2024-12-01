const fs = require("fs");

const start_time = Date.now();

const data = fs.readFileSync("./input.txt", "utf8");
const lines = data.split(/\r?\n/);

let left_side_array = [];
let right_side_array = [];
let result = 0;

for (const line of lines) {
    const l = line.split("   ");
    left_side_array.push(Number(l[0]));
    right_side_array.push(Number(l[1]));
}

left_side_array.sort();
right_side_array.sort();

for (let index = 0; index < left_side_array.length; index++) {
    result += Math.abs(left_side_array[index] - right_side_array[index]);
}

console.log("Result: ", result);
console.log("Run time: ", Date.now() - start_time, "ms");

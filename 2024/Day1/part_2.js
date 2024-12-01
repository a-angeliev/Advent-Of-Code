const fs = require("fs");

const start_time = Date.now();

const data = fs.readFileSync("./input.txt", "utf8");
const lines = data.split(/\r?\n/);

let left_side_array = [];
let right_side_array = [];

for (const line of lines) {
    const l = line.split("   ");
    left_side_array.push(Number(l[0]));
    right_side_array.push(Number(l[1]));
}

let result = 0;

for (let index = 0; index < left_side_array.length; index++) {
    const multiplayer = right_side_array.filter((x) => x === left_side_array[index]).length;
    result += left_side_array[index] * multiplayer;
}
console.log("Result: ", result);
console.log("Run time: ", Date.now() - start_time, "ms");

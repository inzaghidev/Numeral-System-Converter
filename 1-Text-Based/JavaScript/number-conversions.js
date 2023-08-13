function reVal(num) {
  if (num >= 0 && num <= 9) return String.fromCharCode(num + 48);
  else return String.fromCharCode(num - 10 + 65);
}

function fromDeci(base1, inputNum) {
  let s = "";

  while (inputNum > 0) {
    s += reVal(inputNum % base1);
    inputNum = parseInt(inputNum / base1, 10);
  }
  let res = s.split("");

  res.reverse();
  return res.join("");
}

console.log("Konversi Sistem Bilangan dari Desimal");
console.log("Number Base System Converter from Decimal");
console.log("===========================================");

const prompt = require("prompt-sync")(); // some compiler are required this section
let inputNum = prompt("Input Number : ");
let base1 = prompt("Input Base   : ");
console.log(inputNum + "[" + base1 + "] = " + fromDeci(base1, inputNum));

import 'dart:io';

String reVal(int num) {
  if (num >= 0 && num <= 9) {
    return String.fromCharCode(num + '0'.codeUnitAt(0));
  } else {
    return String.fromCharCode(num - 10 + 'A'.codeUnitAt(0));
  }
}

void strev(List<String> str) {
  int len = str.length;
  for (int i = 0; i < len ~/ 2; i++) {
    String temp = str[i];
    str[i] = str[len - i - 1];
    str[len - i - 1] = temp;
  }
}

String fromDeci(String res, int base, int inputNum) {
  int index = 0;

  while (inputNum > 0) {
    res += reVal(inputNum % base);
    inputNum = (inputNum / base).floor();
  }

  List<String> resList = res.split('');
  strev(resList);
  return resList.join('');
}

void main() {
  print("Konversi Sistem Bilangan dari Desimal");
  print("Number Base System Converter from Decimal");
  print("===========================================");

  stdout.write("Input Number : ");
  int inputNum = int.parse(stdin.readLineSync()!);
  stdout.write("Input Base   : ");
  int base = int.parse(stdin.readLineSync()!);
  String res = "";
  print("$inputNum [$base] = ${fromDeci(res, base, inputNum)}");
}

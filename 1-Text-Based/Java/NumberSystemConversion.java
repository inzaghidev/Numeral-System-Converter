import java.lang.*;
import java.io.*;
import java.util.*;
 
class NumberSystemConversion {

static char reVal(int num){
    if (num >= 0 && num <= 9) {
        return (char)(num + 48);
    }
    else {
        return (char)(num - 10 + 65);
    }
}

static String fromDeci(int bse, int inputNum){
    String s = "";

    while (inputNum > 0){
        s += reVal(inputNum % bse);
        inputNum /= bse;
    }
    StringBuilder ix = new StringBuilder();

        ix.append(s);

    return new String(ix.reverse());
}

public static void main (String[] args){
        System.out.println("Konversi Sistem Bilangan dari Desimal");
        System.out.println("Number Base System Converter from Decimal"); 
        System.out.println("===========================================");
        
        Scanner scan = new Scanner(System.in);
        int inputNum, bse;
        
        System.out.print("Input Number : ");
        inputNum = scan.nextInt();
        System.out.print("Input Base : ");
        bse = scan.nextInt();
        
        System.out.println(inputNum+"["+bse+"] = "+fromDeci(bse, inputNum));
    }
}
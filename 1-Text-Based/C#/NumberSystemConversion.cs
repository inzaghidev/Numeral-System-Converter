using System;

class NumberSystemConversion {
    static char reVal(int num){
        if (num >= 0 && num <= 9)
            return (char)(num + 48);
        else
            return (char)(num - 10 + 65);
    }

    static string fromDeci(int bse, int inputNum){
        string s = "";

        while (inputNum > 0){
            s += reVal(inputNum % bse);
            inputNum /= bse;
        }
        char[] res = s.ToCharArray();

        Array.Reverse(res);
        return new String(res);
    }

    static void Main(){
        Console.WriteLine("Konversi Sistem Bilangan dari Desimal");
        Console.WriteLine("Number Base System Converter from Decimal"); 
        Console.WriteLine("===========================================");
        
        int inputNum, bse;
        
        Console.Write("Input Number : ");
        inputNum = Console.Read();
        Console.Write("Input Base : ");
        bse = Console.Read();
        
        Console.WriteLine(inputNum+"["+bse+"] = "+fromDeci(bse, inputNum));
    }
}
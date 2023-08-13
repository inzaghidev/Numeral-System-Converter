#include <stdio.h>
#include <string.h>

char reVal(int num){
    if (num >= 0 && num <= 9){
        return (char)(num + '0');
    }
    else {
        return (char)(num - 10 + 'A');
    }
}

void strev(char *str){
    int len = strlen(str);
    int i;
    for (i = 0; i < len/2; i++){
        char temp = str[i];
        str[i] = str[len-i-1];
        str[len-i-1] = temp;
    }
}

char* fromDeci(char res[], int base, int inputNum){
    int index = 0;
 
    while (inputNum > 0){
        res[index++] = reVal(inputNum % base);
        inputNum /= base;
    }
    res[index] = '\0';
 
    strev(res);
 
    return res;
}

int main(){
    printf("Konversi Sistem Bilangan dari Desimal\n");
    printf("Number Base System Converter from Decimal\n"); 
    printf("===========================================\n");
    
    char res[100];
    int inputNum, base;
    
    printf("Input Number : ");
    scanf("%d", &inputNum);
    printf("Input Base   : ");
    scanf("%d", &base);
    
    printf("%d[%d] = %s\n", inputNum, base, fromDeci(res, base, inputNum));
    return 0;
}
def reVal(num):
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))

def strev(str):
    len = len(str)
    for i in range(int(len / 2)):
        temp = str[i]
        str[i] = str[len - i - 1]
        str[len - i - 1] = temp

def fromDeci(res, base, inputNum):
    index = 0

    while (inputNum > 0):
        res+= reVal(inputNum % base)
        inputNum = int(inputNum / base)

    res = res[::-1]
    return res
    
print("Konversi Sistem Bilangan dari Desimal")
print("Number Base System Converter from Decimal")
print("===========================================")
inputNum = int(input("Input Number : "))
base = int(input("Input Base   : "))
res = ""
print(inputNum,"[",base,"] = ",fromDeci(res, base, inputNum))
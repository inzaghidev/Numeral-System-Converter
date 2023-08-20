import tkinter as tk


def reVal(num):
    if num >= 0 and num <= 9:
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))


def fromDeci(base, inputNum):
    res = ""
    while inputNum > 0:
        res += reVal(inputNum % base)
        inputNum = int(inputNum / base)
    return res[::-1]


def convert():
    inputNum = int(inputNumField.get())
    base = int(baseField.get())
    result = fromDeci(base, inputNum)
    resultField.configure(text=result)


root = tk.Tk()
root.title("Number Base System Converter from Decimal")
root.geometry("400x200")

inputNumLabel = tk.Label(root, text="Input Number:")
inputNumLabel.place(x=20, y=20)
inputNumField = tk.Entry(root)
inputNumField.place(x=150, y=20)

baseLabel = tk.Label(root, text="Input Base:")
baseLabel.place(x=20, y=60)
baseField = tk.Entry(root)
baseField.place(x=150, y=60)

convertButton = tk.Button(root, text="Convert", command=convert)
convertButton.place(x=150, y=100)

resultLabel = tk.Label(root, text="Result:")
resultLabel.place(x=20, y=140)
resultField = tk.Label(root, text="")
resultField.place(x=150, y=140)

root.mainloop()
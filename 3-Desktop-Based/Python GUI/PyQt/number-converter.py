import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton


class NumberSystemConversionGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Base System Converter from Decimal")
        self.setGeometry(100, 100, 400, 200)

        self.inputNumLabel = QLabel("Input Number:", self)
        self.inputNumLabel.move(20, 20)
        self.inputNumField = QLineEdit(self)
        self.inputNumField.move(150, 20)

        self.baseLabel = QLabel("Input Base:", self)
        self.baseLabel.move(20, 60)
        self.baseField = QLineEdit(self)
        self.baseField.move(150, 60)

        self.convertButton = QPushButton("Convert", self)
        self.convertButton.move(150, 100)
        self.convertButton.clicked.connect(self.convert)

        self.resultLabel = QLabel("Result:", self)
        self.resultLabel.move(20, 140)
        self.resultField = QLabel(self)
        self.resultField.move(150, 140)
        self.resultField.resize(200, 30)

    def reVal(self, num):
        if num >= 0 and num <= 9:
            return chr(num + ord("0"))
        else:
            return chr(num - 10 + ord("A"))

    def fromDeci(self, base, inputNum):
        res = ""
        while inputNum > 0:
            res += self.reVal(inputNum % base)
            inputNum = int(inputNum / base)
        return res[::-1]

    def convert(self):
        inputNum = int(self.inputNumField.text())
        base = int(self.baseField.text())
        result = self.fromDeci(base, inputNum)
        self.resultField.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumberSystemConversionGUI()
    window.show()
    sys.exit(app.exec_())

import javax.swing.*;
import java.awt.event.*;

public class NumberSystemConversionGUI extends JFrame {
    private JTextField inputNumField, baseField;
    private JLabel resultField;

    public NumberSystemConversionGUI() {
        setTitle("Number Base System Converter from Decimal");
        setSize(400, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);

        JLabel inputNumLabel = new JLabel("Input Number:");
        inputNumLabel.setBounds(20, 20, 100, 25);
        add(inputNumLabel);

        inputNumField = new JTextField();
        inputNumField.setBounds(150, 20, 150, 25);
        add(inputNumField);

        JLabel baseLabel = new JLabel("Input Base:");
        baseLabel.setBounds(20, 60, 100, 25);
        add(baseLabel);

        baseField = new JTextField();
        baseField.setBounds(150, 60, 150, 25);
        add(baseField);

        JButton convertButton = new JButton("Convert");
        convertButton.setBounds(150, 100, 100, 25);
        convertButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                convert();
            }
        });
        add(convertButton);

        JLabel resultLabel = new JLabel("Result:");
        resultLabel.setBounds(20, 140, 100, 25);
        add(resultLabel);

        resultField = new JLabel("");
        resultField.setBounds(150, 140, 150, 25);
        add(resultField);
    }

    private char reVal(int num) {
        if (num >= 0 && num <= 9) {
            return (char) (num + 48);
        } else {
            return (char) (num - 10 + 65);
        }
    }

    private String fromDeci(int base, int inputNum) {
        StringBuilder res = new StringBuilder();
        while (inputNum > 0) {
            res.append(reVal(inputNum % base));
            inputNum /= base;
        }
        return res.reverse().toString();
    }

    private void convert() {
        int inputNum = Integer.parseInt(inputNumField.getText());
        int base = Integer.parseInt(baseField.getText());
        String result = fromDeci(base, inputNum);
        resultField.setText(result);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new NumberSystemConversionGUI().setVisible(true);
            }
        });
    }
}
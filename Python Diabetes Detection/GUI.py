import sys
import pickle
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt

class Diabetes(QWidget):
    def __init__(self):
        super(Diabetes, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Diabetes Detection")
        self.setFixedSize(600, 400)
        self.labels = ["Glucose:", "Blood Pressure:", "Insulin:", "BMI:", "Age:"]
        self.setupWidgets()

    def setupWidgets(self):
        self.sub_head = QLabel("Patient's Details")
        self.sub_head.setFont(QFont("Times", 24, weight=QFont.Bold))

        self.inputs = []
        self.ranges = []

        for i in range(5):
            label = QLabel(self.labels[i])
            self.inputs.append(QLineEdit())
            self.inputs[i].setValidator(QDoubleValidator())
            self.ranges.append(QLabel(f"(Valid Range: {self.getRange(i)})"))

        self.submit_button = QPushButton("SUBMIT")
        self.submit_button.setFixedWidth(100)
        self.submit_button.clicked.connect(self.testInput)

        self.setupLayout()

    def setupLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.sub_head)
        layout.addSpacing(10)
        layout.setSpacing(5)

        for i in range(5):
            row = QHBoxLayout()
            row.addWidget(self.inputs[i])
            row.addWidget(self.ranges[i])
            layout.addWidget(QLabel(self.labels[i]))
            layout.addLayout(row)

        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def getRange(self, index):
        ranges = ["0-200 mg/dL", "0-130 mm Hg", "0-900 μU/mL", "0-70 meters", "10-100 Years"]
        if 0 <= index < len(ranges):
            return ranges[index]
        else:
            return "Invalid Index"

    # ... (previous code)

    def testInput(self):
        input_dict = {
            "B": float(self.inputs[0].text()),  # Use 'B' instead of 'Glucose'
            "C": float(self.inputs[1].text()),  # Use 'C' instead of 'Blood Pressure'
            "E": float(self.inputs[2].text()),  # Use 'E' instead of 'Insulin'
            "F": float(self.inputs[3].text()),  # Use 'F' instead of 'BMI'
            "H": float(self.inputs[4].text())   # Use 'H' instead of 'Age'
        }

        print("Input Data:", input_dict)  # Add this line
        output = self.checkDiabetes(input_dict)
        if output is not None:
            self.showResult(output)


    # ... (rest of the code)



    def checkDiabetes(self, input_dict):
        try:
            with open('svc.pkl', 'rb') as model:
                p = pickle.load(model)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Model file 'svc.pkl' not found. Train the model first.")
            return None
        except Exception as e:
            print(f"Error loading the model: {e}")
            return None

        # Perform prediction
        df = pd.DataFrame(data=input_dict, index=[0])
        op = p.predict(df)
        return op[0]


    def showResult(self, output):
        if output is not None:
            if output == 0:
                result_text = "No Diabetes Detected."
            else:
                result_text = "Diabetes Detected. Please consult a doctor."

            QMessageBox.information(self, "Diabetes Prediction Result", result_text)

def main():
    app = QApplication(sys.argv)
    window = Diabetes()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

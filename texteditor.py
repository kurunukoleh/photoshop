from PyQt5.QtWidgets import *

def texteditor():
    window = QDialog()

    mainline = QVBoxLayout()

    label = QLabel('введіть текст')
    pole = QLineEdit()
    pole2 = QLineEdit()
    pole3 = QLineEdit()
    button = QPushButton('ок')


    mainline.addWidget(label)
    mainline.addWidget(pole)
    mainline.addWidget(pole2)
    mainline.addWidget(pole3)
    mainline.addWidget(button)

    def returner():
        window.hide()
        window.close()


    button.clicked.connect(returner)

    window.setLayout(mainline)
    window.show()
    window.exec()
    return {"text": pole.text(),
            "x": pole2.text(),
            "y": pole3.text(),}
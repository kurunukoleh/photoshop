from PyQt5.QtWidgets import *

def texteditor():
    window = QDialog()

    mainline = QVBoxLayout()

    label = QLabel('введіть текст')
    pole = QLineEdit()
    label2 = QLabel('введіть коодинати тексту')
    pole2 = QLineEdit()
    pole3 = QLineEdit()
    label3 = QLabel('введіть розмір тексту')
    pole4 = QLineEdit()
    button = QPushButton('ок')


    mainline.addWidget(label)
    mainline.addWidget(pole)
    mainline.addWidget(label2)
    mainline.addWidget(pole2)
    mainline.addWidget(pole3)
    mainline.addWidget(label3)
    mainline.addWidget(pole4)
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
            "y": pole3.text(),
            "size": pole4.text(),}
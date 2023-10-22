from PyQt5.QtWidgets import *

app = QApplication([])

app.setStyleSheet("""
    QWidget {
        background-color:#000000 ;
        color : #ffffff;
        font-size: 15px;
    }

    QPushButton {
        background-color: #ff0000;
        color : #ffffff;
        border-radius: 5px ;
        border-color: #3232ff;
        border-style: hidden;
        border-width: 5px;
        min-height: 20px;
        font-size: 15px;
        font-family: none;

    }


    QListWidget {
        background-color: #141414 ;
        color : #a0a0a0;
        font-size: 15px;
    }

""")

window = QWidget()
window.resize(400 , 300)

mainline = QHBoxLayout()
sline1 = QVBoxLayout()
sline2 = QVBoxLayout()
butonsline = QHBoxLayout()
buton1 = QPushButton('папка')
buton2 = QPushButton('вліво')
buton3 = QPushButton('вправо')
buton4 = QPushButton('дзеркало')
buton5 = QPushButton('різкість')
buton6 = QPushButton('Ч/Б')
pole = QListWidget()
picture = QLabel('ніга буллшит')

sline1.addWidget(buton1)
sline1.addWidget(pole)
sline2.addWidget(picture)
sline2.addLayout(butonsline)
butonsline.addWidget(buton2)
butonsline.addWidget(buton3)
butonsline.addWidget(buton4)
butonsline.addWidget(buton5)
butonsline.addWidget(buton6)
mainline.addLayout(sline1)
mainline.addLayout(sline2)


window.setLayout(mainline)
window.show()
app.exec()
from PyQt5.QtWidgets import *

app = QApplication([])

app.setStyleSheet("""
    QWidget {
        background-color:#000000 ;
        color : #ffffff;
        font-size: 15px;
        min-width: 150px;
        min-height: 300px;
        margin : 10 px;
    }

    QPushButton {
        background-color: #cc0000;
        color : #ffffff;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
        min-width: 100px;
        min-height: 50px;
        font-size: 15px;
        font-family: none;

    }
    
    QPushButton:hover {
        background-color: #ff2200;
        color : #ffffff;
        border-radius: 10px ;
        border-color: #111111;
        border-style: none;
        border-width: 10px;
        min-height: 50px;
        min-width: 100px;
        font-size: 15px;
        font-family: none;

    }
    
    QPushButton#a {
        background-color: #00ff00;
        color : #ffffff;
        border-radius: 5px ;
        border-color: #00ff00;
        border-style: solid;
        min-width: 100px;
        min-height: 50px;
        font-size: 15px;
        font-family: none;

    }
    
    QPushButton#a:hover {
        background-color: #00ff55;
        color : #000000;
        border-radius: 10px ;
        border-color: #00ff55;
        border-style: none;
        border-width: 10px;
        min-height: 50px;
        min-width: 100px;
        font-size: 15px;
        font-family: none;

    }
    
    
    
    QListWidget {
        background-color: #111111 ;
        color : #ffffff;
        font-size: 15px;
        border-color: #000000;
        border-style: none;
        border-width: 1px;
        border-radius: 5px ;
    }
    
    QListWidget:hover {
        background-color: #151515 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
    }
    
     
    QLabel{
        background-color: #000000 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
    }
    
    QLabel:hover{
        background-color: #000000 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
        border-width: 3px;
    }

""")

window = QWidget()
window.resize(800 , 600)

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

buton1.setObjectName('a')

window.setLayout(mainline)
window.show()
app.exec()
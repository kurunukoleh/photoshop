from PIL import Image, ImageEnhance, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
import os


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

app = QApplication([])

app.setStyleSheet("""
    QWidget {
        background-color:#000000 ;
        color : #ffffff;
        font-size: 15px;
        min-width: 1px;
        min-height : 1px;
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
window.resize(800, 600)

mainline = QHBoxLayout()
sline1 = QVBoxLayout()
sline2 = QVBoxLayout()
butonsline1 = QHBoxLayout()
butonsline2 = QHBoxLayout()
buton1 = QPushButton('папка')
buton2 = QPushButton('вліво')
buton3 = QPushButton('вправо')
buton4 = QPushButton('дзеркало')
buton5 = QPushButton('різкість')
buton6 = QPushButton('Ч/Б')
buton7 = QPushButton('яскравіше')
buton8 = QPushButton('контрасніше')
buton9 = QPushButton('контури')

pole = QListWidget()

picture = QLabel('ніга буллшит')

sline1.addWidget(buton1)
sline1.addWidget(pole)
sline2.addWidget(picture)
sline2.addLayout(butonsline1)
sline2.addLayout(butonsline2)
butonsline1.addWidget(buton2)
butonsline1.addWidget(buton3)
butonsline1.addWidget(buton4)
butonsline1.addWidget(buton5)
butonsline2.addWidget(buton6)
butonsline2.addWidget(buton7)
butonsline2.addWidget(buton8)
butonsline2.addWidget(buton9)
mainline.addLayout(sline1)
mainline.addLayout(sline2)

buton1.setObjectName('a')

class workphoto:
    def __init__(self):
        self.image = None
        self.folder = None
        self.filename = None

    def load(self):
        imagePath = os.path.join(self.folder , self.filename)
        self.image = Image.open(imagePath)

    def showImage(self):
        pixel = pil2pixmap(self.image)
        pixel = pixel.scaled(800 , 600  , Qt.KeepAspectRatio)
        picture.setPixmap(pixel)

    def rotateleft(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.showImage()

    def rotateright(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.showImage()

    def mirrow(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.showImage()

    def riskist(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.showImage()

    def blackwhite(self):
        self.image = self.image.convert("L")
        self.showImage()

    def morelight(self):
        self.image = ImageEnhance.Brightness(self.image).enhance(1.5)
        self.showImage()

    def konrast(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(1.5)
        self.showImage()

    def bariers(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.showImage()

photo = workphoto()
buton2.clicked.connect(photo.rotateleft)
buton3.clicked.connect(photo.rotateright)
buton4.clicked.connect(photo.mirrow)
buton5.clicked.connect(photo.riskist)
buton6.clicked.connect(photo.blackwhite)
buton7.clicked.connect(photo.morelight)
buton8.clicked.connect(photo.konrast)
buton9.clicked.connect(photo.bariers)



def opfold():
    photo.folder  = QFileDialog.getExistingDirectory()
    files = os.listdir(photo.folder)
    pole.clear()
    pole.addItems(files)

def shovchooseimage():
    photo.filename = pole.currentItem().text()
    photo.load()
    photo.showImage()


pole.currentRowChanged.connect(shovchooseimage)
buton1.clicked.connect(opfold)
window.setLayout(mainline)
window.show()
app.exec()

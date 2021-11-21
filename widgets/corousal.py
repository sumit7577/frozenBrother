from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import  QMainWindow,QApplication,QWidget,QHBoxLayout,QPushButton,QStyle,QLabel,QFrame
from PyQt5.QtGui import QPixmap
import sys


class Widgets(QMainWindow):
    def __init__(self,parent=None):
        super(Widgets, self).__init__(parent)
        self.counter = 1
        self.setImage = QPixmap(100,100)
        self.setImage.load(f"resource/{self.counter}.png")
        print(self.setImage.height())
        print(self.setImage.width())
        self.leftIcon = self.style().standardIcon(QStyle.SP_ArrowLeft)
        self.rightIcon = self.style().standardIcon(QStyle.SP_ArrowRight)
        self.rect = QRect(0,0,100,100)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        self.Corousal()
        wid.setLayout(self.mainLayout)
        

        
    
    def Corousal(self):
        self.mainLayout = QHBoxLayout()
        self.imageLayout = QHBoxLayout()
        self.textLayout = QHBoxLayout()
        self.image = QLabel()
        self.image.setPixmap(self.setImage)
        self.image.setScaledContents(True)
        self.imageLayout.addWidget(self.image)
        self.mainLayout.addLayout(self.imageLayout)
        self.textLabel = QLabel()
        self.textLabel.setText("something")
        self.imageLayout.addWidget(self.textLabel)
        self.mainLayout.addLayout(self.textLayout)
        self.buttons()


    def buttons(self):
        leftButton = QPushButton()
        rightButton = QPushButton()
        leftButton.clicked.connect(self.clickEventLeft)
        rightButton.clicked.connect(self.clickEventRight)
        rightButton.setGeometry(100,800,30,40)
        rightButton.setIcon(self.leftIcon)
        leftButton.setIcon(self.rightIcon)
        self.mainLayout.addWidget(rightButton)
        self.mainLayout.addWidget(leftButton)

    def clickEventLeft(self):
        self.counter +=1
        self.imageLayout.removeWidget(self.image)
        self.mainLayout.removeItem(self.imageLayout)
        self.setImage = QPixmap(f"resource/{self.counter}.png")
        self.imageLayout = QHBoxLayout()
        self.image = QLabel()
        self.image.setPixmap(self.setImage)
        self.image.setScaledContents(True)
        self.imageLayout.addWidget(self.image)
        self.mainLayout.addLayout(self.imageLayout)



    def clickEventRight(self):
        if(self.counter > 0 ):
            self.counter -= 1
        else:
            self.counter =2
        self.imageLayout.removeWidget(self.image)
        self.mainLayout.removeItem(self.imageLayout)
        self.setImage = QPixmap(f"resource/{self.counter}.png")
        self.imageLayout = QHBoxLayout()
        self.image = QLabel()
        self.image.setPixmap(self.setImage)
        self.image.setScaledContents(True)
        self.imageLayout.addWidget(self.image)
        self.mainLayout.addLayout(self.imageLayout)

        



if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    app = Widgets()
    app.show()
    sys.exit(mainApp.exec_())
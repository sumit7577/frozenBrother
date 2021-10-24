import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QColumnView, QWidget,QVBoxLayout,QHBoxLayout,QPushButton,QGestureEvent,QStyle,QComboBox
from PySide2.QtMultimedia import QMediaContent, QMediaPlayer
from PySide2.QtMultimediaWidgets import QVideoWidget
from qt_material import apply_stylesheet
import sys
from PySide2.QtCore import QEvent, QUrl

# create the application and the main window


class window(QtWidgets.QMainWindow):
    def __init__(self,screen):
        super(window, self).__init__(parent=None)
        self.screen = screen
        self.layout = QVBoxLayout()
        self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        wid = QWidget(self)
        self.setCentralWidget(wid)
        self.layout.addWidget(videoWidget)
        wid.setLayout(self.layout)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.initUi()
        self.pushButtons()
        self.layouts()

    def initUi(self):
        height = self.screen.size().height()
        width = self.screen.size().width()
        self.setGeometry(200, 200,  400 or width,400 or height)
        self.setWindowTitle("Video Player")
        #fileName = QFileDialog.getOpenFileName(self, "Open Movie",QDir.homePath())
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile("topost.avi")))
        self.mediaPlayer.play()

    def pushButtons(self):
        self.playButton = QPushButton()
        self.playButton.setText("Low Danger")
        self.playButton.clicked.connect(self.events)
        self.playButton.setProperty('class', 'success')
        self.playButton1 = QPushButton()
        self.playButton1.setText("Medium Danger")
        self.playButton1.clicked.connect(self.events)
        self.playButton1.setProperty('class', 'warning')
        self.playButton2 = QPushButton()
        self.playButton2.setText("High Danger")
        self.playButton2.clicked.connect(self.events)
        self.playButton2.setProperty('class', 'danger')

    def layouts(self):
        self.controlLayout = QHBoxLayout()
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.controlLayout.addWidget(self.playButton)
        self.controlLayout.addWidget(self.playButton1)
        self.controlLayout.addWidget(self.playButton2)
        self.layout.addLayout(self.controlLayout)


    def events(self):
        self.layout.removeItem(self.controlLayout)
        widgets = QComboBox()
        widgets.insertItems(0,["something","something2","something 3","something 4"])
        self.extraLayout = QHBoxLayout()
        self.extraLayout.addWidget(widgets)
        self.layout.addLayout(self.extraLayout)
        self.extraLayout.setContentsMargins(0, 0, 0, 0)
        
    
    


# setup stylesheet


# run
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    screen = app.primaryScreen()
    windower = window(screen)
    windower.show()
    sys.exit(app.exec_())

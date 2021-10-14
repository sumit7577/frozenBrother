from PyQt5.QtWidgets import QMainWindow,QApplication,QGridLayout,QFileDialog
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QDir, Qt, QUrl
import sys 
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
class window(QMainWindow):
    def __init__(self,screen,parent=None):
        super(window,self).__init__(parent)
        self.screen = screen
        self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.initUi()

    def initUi(self):
        height = self.screen.size().height()
        width = self.screen.size().width()
        self.setGeometry(200,200,400 or width,400 or height)
        self.setWindowTitle("Video Player")
        fileName = QFileDialog.getOpenFileName(self, "Open Movie",QDir.homePath())
        self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName[0])))
        self.mediaPlayer.play()
    
    def setVideo(self):
        pass

    def layout(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    myWindow = window(screen)
    myWindow.show()
    myWindow.setVideo()
    sys.exit(app.exec_())

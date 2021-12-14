from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class PyToggle(QCheckBox):
    def __init__(self,Parent, width=60, bg_color="#777", circle_color="#DDD", active_color="#00BCff"):
        QCheckBox.__init__(self,parent=Parent)
        self.setFixedSize(width, 28)
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.bg_color = bg_color
        self.circle_color = circle_color
        self.actice_color = active_color
        self.stateChanged.connect(self.debug)

    def debug(self):
        print(self.isChecked())

    def hitButton(self, pos: QtCore.QPoint) -> bool:
        return self.contentsRect().contains(pos)

    def paintEvent(self, a0):
        p = QPainter(self)
        p.setPen(Qt.PenStyle.NoPen)
        

        # draw circle
        if not self.isChecked():
            p.setBrush(QColor(self.bg_color))
            p.drawRect(0, 0, 100, 100)
            p.setBrush(QColor(self.circle_color))
            p.drawRect(3, 3, 22, 22)
            
        else:
            p.setBrush(QColor(self.actice_color))
            p.drawRect(0, 0, 100, 100)
            p.setBrush(QColor(self.circle_color))
            p.drawRect(30, 3, 22, 22)

        p.end()


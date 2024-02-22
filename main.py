from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.resize(100, 100)
        self.pushButton.clicked.connect(self.circle)
        self.label = QLabel()
        self.label.setPixmap(QPixmap(600, 600))

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 255, 0))
        painter.setPen(pen)
        painter.drawEllipse(*[randint(10, 500) for i in range(2)], *[randint(10, 100) for i in range(2)])
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    git = Circles()
    git.show()
    sys.exit(app.exec_())
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie

size_xy = [200, 400]
class Sticker(QtWidgets.QMainWindow):
    def __init__(self, img_path, xy, size=1.0, on_top=False):
        super(Sticker, self).__init__()
        self.timer = QtCore.QTimer(self)
        self.img_path = img_path
        self.xy = xy
        self.from_xy = xy
        self.from_xy_diff = [0, 0]
        self.to_xy = xy
        self.to_xy_diff = [0, 0]
        self.speed = 60
        self.direction = [0, 0] # x: 0(left), 1(right), y: 0(up), 1(down)
        self.size = size
        self.on_top = on_top
        self.localPos = None

        self.setupUi(img_path)
        self.show()

    # 포인터 움직임 발생 시
    def mouseMoveEvent(self, event):
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.xy = [event.globalX() - size_xy[0], event.globalY() - size_xy[1]]
        #self.xy = [(event.globalX() - self.localPos.x()), (event.globalY() - self.localPos.y())]
        self.move(*self.xy)
        print(self.xy)


    def setupUi(self, image):
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)
        centralWidget.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setMouseTracking(True)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint if self.on_top else QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        label = QtWidgets.QLabel(centralWidget)
        pixmap = QtGui.QPixmap(image)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())

        self.setGeometry(self.xy[0], self.xy[1], pixmap.width(), pixmap.height())
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    s = Sticker('study.jpeg', xy=[0, 0], on_top=True)

    sys.exit(app.exec_())

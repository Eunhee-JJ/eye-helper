import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import cv2
import pyautogui as pag

size_xy = [140, 90]
class Sticker(QtWidgets.QMainWindow):
    def __init__(self, img_path, xy, size=1.0, on_top=False):
        super(Sticker, self).__init__()
        self.timer = QtCore.QTimer(self)
        self.img_path = img_path
        self.xy = xy
        self.size = size
        self.on_top = on_top
        self.localPos = None

        self.setupUi(img_path)
        self.show()

    # 포인터 움직임 발생 시
    def mouseMoveEvent(self, event):
        self.xy = [event.globalX() - size_xy[0], event.globalY() - size_xy[1]]
        self.move(*self.xy)
        self.capture()
        print(self.xy)

    def capture(self):
        # 캡쳐 경로와 이름을 지정한다
        # 스크린샷
        pag.screenshot(self.img_path, region=(self.xy[0], self.xy[1], size_xy[0], size_xy[1]))
        img_source = cv2.imread(self.img_path)
        # 2배 이미지
        img_result = cv2.resize(img_source, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        cv2.imwrite('capture.png', img_result)

    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent):
        QtWidgets.qApp.quit()

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
    position = pag.position()  # 여기다가 HYE좌표 넣어주자
    x = position.x
    y = position.y
    s = Sticker('capture.png', xy=[x, y], on_top=True)

    sys.exit(app.exec_())

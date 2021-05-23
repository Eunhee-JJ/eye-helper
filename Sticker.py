import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import cv2
import pyautogui as pag
import threading
import multiprocessing as mp
from multiprocessing import Process, Queue
import zoom_zoom

size_xy = [140, 90]
pointer_xy = zoom_zoom.left_top
img = 'capture.png'


# 좌표 부근 스크린샷 후 확대
def capture(xy):
    proc = mp.current_process()
    print(proc.name)
    pag.screenshot(img, region=(xy[0], xy[1], size_xy[0], size_xy[1]))
    img_source = cv2.imread(img)
    img_result = cv2.resize(img_source, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(img, img_result)


# 프레임 없는 윈도우 창
class Sticker(QtWidgets.QMainWindow):
    def __init__(self, img_path, xy, size=1.0, on_top=False):
        super(Sticker, self).__init__()
        self.img_path = img_path
        self.xy = xy
        self.size = size
        self.on_top = on_top

        self.setupUi(img_path)
        self.show()

    # 포인터 움직임 발생 시(임시) -> 좌표값 생성될 때마다 실행되도록 변경해줘야 함
    '''
    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents) # 마우스 이벤트 무시
        self.xy = [event.globalX() - size_xy[0], event.globalY() - size_xy[1]]
        self.move(*self.xy)
        print(self.xy)
        p2 = Process(name="capture", target=capture, args=(pointer_xy,), daemon=True)
        p2.start()
    '''

    # 좌표값 이용하는 방법으로 변경한 예시
    def stickerMove(self, p_xy):
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)  # 마우스 이벤트 무시
        super().setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.xy = [p_xy[0] - size_xy[0], p_xy[1] - size_xy[1]]
        self.move(*self.xy)

    # def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent):
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        QtWidgets.qApp.quit()

    def setupUi(self, image):
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)
        centralWidget.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        # self.setMouseTracking(True)

        flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint if self.on_top else QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        label = QtWidgets.QLabel(centralWidget)
        pixmap = QtGui.QPixmap(image)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        while True:
            p = mp.Process(name="capture", target=capture, args=(pointer_xy,))
            p.start()
            p.join()
            QtWidgets.QApplication.processEvents()
            self.stickerMove(self.xy)
            self.setGeometry(self.xy[0], self.xy[1], pixmap.width(), pixmap.height())
            self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    s = Sticker(img, xy=[pointer_xy[0] - size_xy[0], pointer_xy[1] - size_xy[1]], on_top=True)
    sys.exit(app.exec_())
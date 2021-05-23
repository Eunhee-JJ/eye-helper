import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import cv2
import pyautogui as pag
import threading

img = 'c.png'
pag.screenshot(img, region=(0, 0, 200, 159))
img_source = cv2.imread(img)
img_result = cv2.resize(img_source, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imwrite(img, img_result)

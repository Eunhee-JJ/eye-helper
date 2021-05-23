from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import re
import pickle
import numpy as np
import pyautogui as pag
import cv2
import sys
import Sticker


def zoom_exec(mode:int):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('E:\Data Structure\GazePointer_API\chromedriver.exe',options=options)
    driver.implicitly_wait(3)
    driver.get('E:\Data Structure\GazePointer_API\GazePointer.html')
    screen_array = np.load('screen_array.npy', allow_pickle=True)
    screen_hash_4_pickle = open("screen_hash_4.pkl", "rb")
    screen_hash_4 = pickle.load(screen_hash_4_pickle)
    screen_hash_4_pickle.close()
    screen_hash_5_pickle = open("screen_hash_5.pkl", "rb")
    screen_hash_5 = pickle.load(screen_hash_5_pickle)
    screen_hash_5_pickle.close()
    sleep(5)

    while(True):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        GazeData = soup.select_one('#GazeData').text
        GazeData_numbers = re.findall("\d+", GazeData)
        HeadPhoseData = soup.select_one('#HeadPhoseData').text
        HeadPhoseData_numbers = re.findall(r"[-+]?\d*\.\d+|\d+", HeadPhoseData)
        HeadRotData = soup.select_one('#HeadRotData').text
        HeadRotData_numbers = re.findall(r"[-+]?\d*\.\d+|\d+", HeadRotData)
        '''print("※※※※※※※※※※※※※※※※※※※※※※※※※※※")
        print(GazeData)
        print(GazeData_numbers) #x,y
        print("Hash String :", end=" ")'''
        try:
            if mode == 5:
                hash_string = int(screen_array[int(GazeData_numbers[1])][int(GazeData_numbers[0])])
            else:
                hash_string = int(screen_array[int(GazeData_numbers[1])][int(GazeData_numbers[0])][0:-1])
            '''print(hash_string)'''
            '''hash_string = hash_string[:-1]
            print(hash_string)'''
        except:
            print("Failed to load Hash string")

        # 위에 구한값을 변수에 담아둔다
        left_top = (int(screen_hash_4[hash_string][2]), int(screen_hash_4[hash_string][0])) #x,y
        right_bottom = (int(screen_hash_4[hash_string][3]), int(screen_hash_4[hash_string][1])) #x,y

        # 좌측상단의 x, 우측하단의 y값을 저장해둔다
        left_top_x = left_top[0]
        right_bottom_y = right_bottom[1]

        # 캡쳐 범위의 폭과 높이를 구한다
        capture_width = right_bottom[0] - left_top[0]
        capture_height = right_bottom[1] - left_top[1]

        app = Sticker.QtWidgets.QApplication(sys.argv)
        s = Sticker(Sticker.img, xy=[pointer_xy[0] - size_xy[0], pointer_xy[1] - size_xy[1]], on_top=True)
        sys.exit(app.exec_())

        sleep(1)
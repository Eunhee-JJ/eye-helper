from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import re
import pickle
import numpy as np
import pyautogui as pag
import cv2
from tkinter import *
from time import time

def zoom_exec(mode:int):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('chromedriver.exe',options=options)
    driver.implicitly_wait(3)
    driver.get('C:\GazePointer.html')
    screen_array = np.load('screen_array.npy', allow_pickle=True)
    screen_hash_2_pickle = open("screen_hash_2.pkl", "rb")
    screen_hash_2 = pickle.load(screen_hash_2_pickle)
    screen_hash_2_pickle.close()
    screen_hash_3_pickle = open("screen_hash_3.pkl", "rb")
    screen_hash_3 = pickle.load(screen_hash_3_pickle)
    screen_hash_3_pickle.close()
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
            elif mode == 4:
                hash_string = int(screen_array[int(GazeData_numbers[1])][int(GazeData_numbers[0])][0:-1])
            elif mode == 3:
                hash_string = int(screen_array[int(GazeData_numbers[1])][int(GazeData_numbers[0])][0:-2])
            else:
                hash_string = int(screen_array[int(GazeData_numbers[1])][int(GazeData_numbers[0])][0:-3])
            '''print(hash_string)'''
            '''hash_string = hash_string[:-1]
            print(hash_string)'''
        except:
            print("Failed to load Hash string")
        '''print("Region to Zoom :", end=" ")
        print(screen_hash_4[hash_string]) #y, y+h, x, x+w
        print(type(screen_hash_4[hash_string][0]))'''
        '''except:
            print("Faile to load Region to zoom")'''
        '''print(HeadPhoseData)
        print(HeadPhoseData_numbers)
        print(HeadRotData)
        print(HeadRotData_numbers)
        print("※※※※※※※※※※※※※※※※※※※※※※※※※※※")'''

        '''position = pag.position()  # 여기다가 HYE좌표 넣어주자
        x = position.x
        y = position.y
        print(position)'''
        # 위에 구한값을 변수에 담아둔다
        if mode == 5:
            left_top = (int(screen_hash_5[hash_string][2]), int(screen_hash_5[hash_string][0])) #x,y
            right_bottom = (int(screen_hash_5[hash_string][3]), int(screen_hash_5[hash_string][1])) #x,y
        elif mode == 4:
            left_top = (int(screen_hash_4[hash_string][2]), int(screen_hash_4[hash_string][0])) #x,y
            right_bottom = (int(screen_hash_4[hash_string][3]), int(screen_hash_4[hash_string][1])) #x,y
        elif mode == 3:
            left_top = (int(screen_hash_3[hash_string][2]), int(screen_hash_3[hash_string][0])) #x,y
            right_bottom = (int(screen_hash_3[hash_string][3]), int(screen_hash_3[hash_string][1])) #x,y
        else:
            left_top = (int(screen_hash_2[hash_string][2]), int(screen_hash_2[hash_string][0])) #x,y
            right_bottom = (int(screen_hash_2[hash_string][3]), int(screen_hash_2[hash_string][1])) #x,y


        # 좌측상단의 x, 우측하단의 y값을 저장해둔다
        left_top_x = left_top[0]
        right_bottom_y = right_bottom[1]

        # 캡쳐 범위의 폭과 높이를 구한다
        capture_width = right_bottom[0] - left_top[0]
        capture_height = right_bottom[1] - left_top[1]

        # 캡쳐 경로와 이름을 지정한다
        path = "capture.png"
        # 스크린샷
        '''print(left_top)
        print(left_top_x)
        print(right_bottom_y)
        print(capture_width)
        print(capture_height)'''
        pag.screenshot(path, region=(left_top_x, right_bottom_y, capture_width, capture_height))

        '''# 원본 이미지
        img_source = cv2.imread('capture.png')
        cv2.imshow("original", img_source)
    
        cv2.waitKey(0)'''

        img_source = cv2.imread('capture.png')
        # 2배 이미지
        img_result = cv2.resize(img_source, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        cv2.imwrite('capture.png', img_result)
        '''cv2.namedWindow("x2", flags=cv2.WINDOW_GUI_NORMAL)
        cv2.imshow("x2", img_result)
        cv2.moveWindow("x2",left_top[0],left_top[1])'''

        root = Tk()

        # Adjist size
        if mode == 5:
            root.geometry("120x64+%d+%d" %(left_top[0],left_top[1]))
        elif mode == 4:
            root.geometry("240x135+%d+%d" %(left_top[0],left_top[1]))
        elif mode == 3:
            root.geometry("478x268+%d+%d" %(left_top[0],left_top[1]))
        else:
            root.geometry("958x538+%d+%d" %(left_top[0],left_top[1]))
        # Use overrideredirect() method
        root.overrideredirect(True)
        # Execute tkinter
        start = time()
        root.after(500, root.destroy)
        wall = PhotoImage(file="capture.png")
        wall_label = Label(image=wall)
        wall_label.place(x=-2, y=-2)
        root.mainloop()
        end = time()
        '''root = Tk()
        root.geometry("400*400")
        root.overrideredirect(True)
        root.mainloop()'''

        #cv2.waitKey(100)

        '''# 4배 이미지
        height, width = img_source.shape[:2]
        img_result = cv2.resize(img_source, (4*width, 4*height), interpolation = cv2.INTER_LINEAR )
        cv2.imshow("x4 INTER_LINEAR", img_result)
    
        height, width = img_source.shape[:2]
        img_result2 = cv2.resize(img_source, (4*width, 4*height), interpolation = cv2.INTER_CUBIC )
        cv2.imshow("x4 INTER_CUBIC", img_result)
    
        cv2.waitKey(0)
    
    
        
        img_result = cv2.resize(img_result2, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
        cv2.imshow("x0.5 INTER_AREA", img_result)
    
        img_result = cv2.resize(img_result2, None, fx=0.5, fy=0.5) # cv2.INTER_LINEAR
        cv2.imshow("x0.5 INTER_LINEAR", img_result)
    
        cv2.waitKey(0)
        '''

        #cv2.destroyAllWindows()


        #sleep(1)

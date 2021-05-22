import pyautogui as pag
import cv2

### 그 링크 코드랑 거의 똑같고 좌표 넣는 부분이랑 cv2.INTER_LINEAR 만 수정함

# 캡쳐할 영역의 왼쪽 상단 모서리와 오른쪽 하단 모서리의 좌표값을 미리구해둔다.

position = pag.position() #여기다가 HYE좌표 넣어주자
x=position.x
y=position.y
print(position)
#위에 구한값을 변수에 담아둔다
left_top = (x, y)
right_bottom = (x+100, y+100)

#좌측상단의 x, 우측하단의 y값을 저장해둔다
left_top_x = left_top[0]
right_bottom_y = right_bottom[1]

#캡쳐 범위의 폭과 높이를 구한다
capture_width = right_bottom[0]-left_top[0]
capture_height = right_bottom[1]-left_top[1]

#캡쳐 경로와 이름을 지정한다
path = "capture.png"
#스크린샷
pag.screenshot(path, region=(left_top_x, right_bottom_y, capture_width, capture_height))

'''# 원본 이미지
img_source = cv2.imread('capture.png')
cv2.imshow("original", img_source)

cv2.waitKey(0)'''

img_source = cv2.imread('capture.png')
# 2배 이미지
img_result = cv2.resize(img_source, None, fx=2, fy=2, interpolation = cv2.INTER_LINEAR)
cv2.imshow("x2", img_result)

cv2.waitKey(0)


'''# 4배 이미지
height, width = img_source.shape[:2]
img_result = cv2.resize(img_source, (4*width, 4*height), interpolation = cv2.INTER_LINEAR )
cv2.imshow("x4 INTER_LINEAR", img_result)

height, width = img_source.shape[:2]
img_result2 = cv2.resize(img_source, (4*width, 4*height), interpolation = cv2.INTER_CUBIC )
cv2.imshow("x4 INTER_CUBIC", img_result)

cv2.waitKey(0)


# INTER_CUBIC를 사용해 확대한 4배 이미지를 0.5배한 이미지
img_result = cv2.resize(img_result2, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
cv2.imshow("x0.5 INTER_AREA", img_result)

img_result = cv2.resize(img_result2, None, fx=0.5, fy=0.5) # cv2.INTER_LINEAR
cv2.imshow("x0.5 INTER_LINEAR", img_result)

cv2.waitKey(0)
'''

cv2.destroyAllWindows()

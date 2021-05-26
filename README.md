# eye-helper
2021 자료구조 팀플 - Hash 적용

## 아이트래킹 → 크롤링 → 해싱

  0. 배열, 딕셔너리 만들고 GazePointer api 활용한거 (프로그램이 윈도우에서만 돌아감..)

[make_numpy_screen_array.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a1cbe884-c3dd-4e5d-8a8a-ae6c2dad2a92/make_numpy_screen_array.py)

여기서 픽셀마다 스트링 (ex : 01232) 저장해주고... (배열 npy로 저장)

[screen_hash.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d952329f-857a-4168-a4ba-6b6ba272097b/screen_hash.py)

여기서 문자열 4개짜리, 5개짜리 딕셔너리 만들어주고...

(ex : 01232 → 확대할 좌표) (딕셔너리 pkl로 저장)

[API.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5380ef7c-4c6c-4436-9883-999629b6eca3/API.py)

[GazePointer.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/21112de2-32d1-41f9-85bb-6be2c062f0f5/GazePointer.html)

javascript api 찾은거 selenium으로 크롤링 해서 파이썬으로 가져와서 씀

(과정 : 내가 보는 곳 → 스트링 → 확대할 곳)

## 돋보기

1. ~~포인터 좌표 받아오기 => 크롤링o~~
2. 좌표 부근 스크린샷
    - Pyautogui, pil
    - [https://tmizip.tistory.com/11](https://tmizip.tistory.com/11)

3. 스크린샷 확대
    - Opencv
    - [https://webnautes.tistory.com/m/1251](https://webnautes.tistory.com/m/1251)

4. 스크린샷 띄우기
    - pyqt 스티커
    - [https://youtu.be/K1ryq4vG_Pg](https://youtu.be/K1ryq4vG_Pg)
        - gif → jpg(movie → pixmap)
        - [https://notstop.co.kr/501/](https://notstop.co.kr/501/)
        - setMouseTracking(True)
        - [https://has3ong.tistory.com/199](https://has3ong.tistory.com/199)
        - 

5. 클릭(비동기/병렬) 가능하도록 처리
    - Pyqt slot(=콜백)

+) 키보드 이벤트로 돋보기 on/off 기능 넣으면 좋을 듯

# 보조기억장치의 필요성

# 메모리는 용량이 작고 전원을 끄면 데이터를 잃는다.
# 보조기억장치는 용량이 크고 전원을 꺼도 데이터를 보관할 수 있다.

# 파일
# 보조기억장치에 데이터를 저장하는 기본 단위

# 텍스트 파일 입출력
# 1. 파일 열기
# 2. 데이터를 파일에 쓰거나, 파일로부터 읽어오기
# 3. 파일 닫기 -> 운영체제에게 파일 사용이 끝났음을 알리기

# "wt" : write text
# myfile = open("myfile.txt", "wt")
# myfile.write("Hello, World!")
# myfile.close()

# 파일이 없는 경우에 예외처리를 할 수 있도록,
# 오류가 있어도 프로그램이 우선 돌 수 있도록 해야함
try:
    myFile = open("myfile.txt")
except FileNotFoundError as e:
    print("예외가 발생하였습니다.", e)
    
# 파이썬이 파일을 찾을 때는 현재 작업중인 디렉토리에서 찾기 시작한다.

import os
print(os.getcwd())

# 윈도우와 맥 OS의 경로 표현이 다르다
# 윈도우는 역슬래시(\)를 사용하고, 맥은 슬래시(/)를 사용한다.

# os.path.join(os.getcwd(), "myfile.txt")

# with-as
# 문맥 관리자라고도 한다.
# context manager라고도 한다.


######################## Recursion ########################

def func1():
    print("func1")

def func2():
    func1()
    print("func2")

func2()

# 어떤 함수 안에서 자기 자신을 호출하기

def my_func(count):
    # 재귀함수의 무한 루프를 경계해야 함
    # 재귀함수가 기술적으로 내 안에서 도는 것은 아니다.
    # 실시간으로 다른 프레임을 만들어서 실행하는 것이다. id()를 확인하면 함수의 주소가 다른 것을 확인할 수 있음
    if count > 0:
        # 재귀 호출에는 종료 조건을 명시적으로 넣어주는 것이 중요
        print(count)
        my_func(count - 1)
    else:
        print("Done")
        
my_func(10)


# 팩토리얼

def factorial(n):
    if n == 0:
        return 1
    if n >= 1:
        return n* factorial(n-1)
    
for n in range(0, 11):
    print(factorial(n), end=" ")
    
print(" ")
    
# 피보나치

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(0,11):
    print(fibonacci(n), end=" ")


######################## 함수 객체 Function Object ########################

# 파이썬에서는 함수도 객체다
# 함수도 변수로 저장할 수 있음
# 함수 객체를 변수가 가리킬 수 있는 것이다.

from datetime import datetime

def print_date():
    today = datetime.now()
    print(today)
    
def print_time():
    current_time = datetime.now()
    print(current_time)
    
# 함수를 객체처럼 사용할 수 있기 때문에 딕셔너리에 함수 자체를 저장해서 사용할 수 있음 
command_callbacks = {"날짜": print_date, "시간": print_time}

user_command = input("날짜 또는 시간을 입력하세요: ")

#command_callbacks[user_command]()

# 함수 객체를 파라미터(인수)로 전달하기

def print_func(func):
    func()
    
print_func(print_date)

# 함수 객체를 리턴하기

def return_func():
    return print_date

my_func = return_func()
my_func()

# Closer
# 함수안에 정의된 내부적으로 정의된 함수를 지칭함 
def outer_func():
    x = 10
    def inner_func():
        print(x)
    return inner_func

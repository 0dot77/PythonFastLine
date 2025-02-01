######################## Call by Object Reference #########################

def my_func(a):
    a += 100
    
    return a

x = 1
# print(x)

result = my_func(x)

# print(x)
# print(result)


# 매개변수가 가변 객체일 경우

def append_hello(func_list):
    print("IN", id(func_list))
    func_list.append("Hello")
    return func_list
    
my_list = ["a"]

# print("Before", id(my_list))

# 얕은 복사 shallow copy
# 원본 객체의 주소를 복사
new_list = append_hello(my_list.copy())

# 깊은 복사 deepcopy
# 완전히 새로운 객체를 만들어서 복사
# 단점은 메모리를 많이 차지함 -> 메모리를 많이 쓴다면, 사본을 만드는데에 조심해야함
#new_deep_list = append_hello(my_list.deepcopy())

# print("After", id(my_list))

# print(my_list)

# 함수가 반환을 할 때도 객체의 참조를 반환함
# 새로 객체를 만드는 것보다 효율적임

def make_list():
    temp = []
    # 여기서 id는 함수가 반환하는 객체의 주소를 반환함
    print(id(temp))
    return temp

new_list_1 = make_list()

#print(id(new_list_1))

# [주의] 가변 객체를 인수로 넣어줄 때
# 기본값의 객체가 계속 재사용된다.
def f(a, my_list = []):
    my_list.append(a)
    return my_list

print(f(1))
print(f(2))
print(f(3))

######################## Scope (local variable, global variable) #########################
# 함수 안에서 정의된 변수를 지역 변수 

def my_func1():
    x = ["A"]
    print(x, id(x))
    
def my_func2():
    x = ["B"]
    print(x, id(x))
    
my_func1()
my_func2()

# 함수 밖에서 정의된 변수를 전역 변수

y = 10

def my_func3():
    print(y)
    
def my_func4():
    y = 20
    print(y)
    
my_func3()
my_func4()

# 전역 변수와 지역 변수가 이름이 다를 때는 함수 안에서 둘 다 사용가능하다.

x = 1

def my_func5():
    x = 10
    print(x)
    
my_func5()

# 함수 호출 이후에는 1이 출력된다.
# 파이썬 입장에서는 완전히 다른 변수다.
print(x)

# global 키워드
# 함수 안에서 전역 변수를 지역 변수처럼 사용하고자 할 때

def my_func6():
    global x
    x = 100
    print(x)
    
my_func6()

# 전역변수 x 값이 반영된다.
print(x)

# 파이썬에서는 함수도 객체다.

######################## LEGB Rule ########################
# Local, Enclosed, Global, Built-in

# 빌트인 함수와 동일한 이름은 지양하기
# Local Scope 함수가 가장 우선 순위가 높음
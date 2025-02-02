######################## Lamda ########################

# 이름이 없는 함수
# lamda expression 

my_func = lambda x, y : x + y

print(my_func(1, 2))

# map(), filter()와 같은 내장 함수와 쓸 때 편리함

add_100 = lambda x : x + 100

# map()의 결과를 list 컨테이너에 넣어서 사용할 수 있도록 함
list(map(add_100, [1,2,3,4]))

list(map(lambda x, y : x + y, [1,2,3,4], [5,6,7,8]))

# filter() 주어진 조건에 따라 이터러블 요소들을 걸러준다.
# 반환값이 true면 포함시키는 구조
list(filter(lambda x : x % 2 == 0, [1,2,3,4,5]))


# reduce() 함수는 주어진 함수를 시퀀스에 반복적으로 적용하여 하나의 값으로줄여준다.

from functools import reduce

add = lambda x, y : x + y

# 값이 하나가 될 때까지 반복한다.
print(reduce(add, [1,2,3,4,5]))

# sorted() 함수에 정렬 기준을 정할 때도 람다를 사용할 수 있음
my_dict = {"apple": 3, "Alpha" : 100, "Drive" : 10, "data":33, "Billy":50}

# 딕셔너리를 반환하면서, 정렬할 때 값을 기준으로 정렬한다는 말임
# 즉, 값에 따라서 그 정렬의 기준이 세워지는 것
print(dict(sorted(my_dict.items(), key=lambda item:item[1])))

# 자리수 합치기

# def add_digits(num:int) -> int:
#     print(num)
    
#     if num < 10:
#         return num
#     else:
#         return add_digits(sum([int(x) for x in str(num)]))
    
# add_digits(13567)

def add_digits(num:int) -> int:
    print(num)
    
    if num < 10:
        return num
    else:
        return add_digits(reduce(lambda x, y : int(x) + int(y), str(num)))
    
add_digits(13567)

######################## Docstring ########################

# 함수나 클래스를 문서로 설계하는 것이 중요함
# top->down으로 구현하는 방식

def talk_to_ai(user_input:str)->str:
    """ 사용자의 대사를 인공지능에게 전달해주고 대답을 받는다.
    
    Args:
        user_input: 사용자의 대사
        
    Returns:
        str: 인공지능의 대답
    """
    pass


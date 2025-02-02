# find the word "Alice"
with open("Chapter5/alice_in_wonderland.txt", "rt") as f:
    read_data = f.read()

splitted = read_data.split()

count = 0

for w in splitted:
    if 'alice' in w.lower():
        count += 1
    
print(count)

# 정규식 사용하기

import re

# re.IGNORECASE : 대소문자 구분 없이 검색
res = len(re.findall('Alice', read_data, re.IGNORECASE))

print(res)

# 어떤 알파벳이 많이 쓰였는지 세어보기

counter_ab = {}

for l in read_data.lower():
    if l.isalpha():
        counter_ab[l] = counter_ab.get(l, 0) + 1

counter_ab = {k : v for k, v in sorted(counter_ab.items(), key=lambda item: item[1], reverse=True)}

#print(list(counter_ab.keys())[0])

#print(counter_ab)

from collections import Counter

read_dict = {
    k: v  # 키-값 쌍에서의 문자(k)와 빈도수(v)
    for k, v in sorted(  # 정렬된 결과를 순회
        # 1. Counter로 문자 빈도수 계산 (소문자 통일)
        # 2. items()로 (문자, 빈도수) 튜플 리스트 생성
        Counter(read_data.lower()).items(),
        # 정렬 기준: 빈도수(item[1])를 기준으로 내림차순
        key=lambda item: item[1],
        reverse=True
    )
    # 필터링 조건: 알파벳 문자만 처리 (특수문자/공백 제외)
    if k.isalpha()
}

print(read_dict)
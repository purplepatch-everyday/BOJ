"""
1157번: 단어 공부 

문제: 단어 안에서 가장 많이 쓰인 letter 출력하기 (단, 대소문자 구별 x)

input: 대소문자로 이루어진 단어

output: 가장 많이 사용된 알파벳 "대문자로" 출력 (단, 여러개 존재한다면 ? 출력) 
"""
"""
TEST CASE 1: Mississipi
OUTPUT 1: ?

TEST CASE 2: zZa
OUTPUT 2: Z
"""
import sys 

# input 받으면서 대문자로 변경하기
input_word = input().upper()

# 알파벳으로 변경
letters = []
for i in input_word: 
    letters.append(i)

#중복 제거 
check = set(letters)

#각각 몇개있는지 체크 
letter_count= {}
for letter in check: 
    letter_count[letter] = letters.count(letter)

max_letter_count = max(letter_count.values())

# max value 찾기 
result =[]
for key,value in letter_count.items():
    if value == max_letter_count:
        result.append(key)

if len(result) > 1:
    print("?")
else:
    print(*result)
    
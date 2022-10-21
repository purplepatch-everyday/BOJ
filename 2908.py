"""
2908번: 상수

문제: 주어진 두 숫자를 각각 거꾸로 읽고 그 중 큰 수를 출력한다

input: 세자리의 두 숫자

output: 거꾸로 읽은 숫자 중 큰 수 출력 
"""
"""
TEST CASE 1: 734 893
OUTPUT 1: 437

TEST CASE 2: 221 231
OUTPUT 2: 132

TEST CASE 3: 839 237
OUTPUT 3: 938
"""

# input 받기 
import sys

input_numbers = list(input().split())

# 문자열 안에있는 index 별로 거꾸로 읽기
result = []
for num in input_numbers: 
    reverse_number = num[::-1]
    result.append(reverse_number)

# 거꾸로된 숫자를 비교하여 더 큰 숫자 출력하기 (2개 밖에 없기 때문에 그냥 if로 비교 가능)
if result[0]>result[1]:
    print(result[0])
else: 
    print(result[1])

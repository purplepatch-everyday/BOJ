"""
2163번: 초콜릿 자르기

문제: 초콜릿 원하는 크기로 자를 때 최소로 드는 쪼개기 횟수 

input: 
첫째줄에 두 정수 

output: 두 정수이 크기로 만들기 위해 최소로 드는 횟수 

"""
"""
TEST CASE 1: 2 2
OUTPUT 1: 3

TEST CASE 2: 1 1
OUPUT 2: 0  
"""

# input 받기 
# 2개만 받기 때문에 number 1,2로 받는다
num1, num2 = input().split()

if int(num1) == 1 and int(num2)==1:
    result = 0 
else:
    result = int(num1) * int(num2) -1 

print(result)
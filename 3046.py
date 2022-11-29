"""
3046번: R2

문제: R1(숫자 한개)와 S(평균)이 주어질때 다른 숫자 출력하기 

input: 
첫째줄에 두 정수 

output: R2 출력

"""
"""
TEST CASE 1: 11 15
OUTPUT 1: 19

TEST CASE 2: 4 3
OUPUT 2: 2 
"""

# input 받기 
input_num1, input_num2 = input().split()

result = (int(input_num2) *2) - int(input_num1)

print(result)
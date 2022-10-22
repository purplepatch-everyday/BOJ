"""
5622번: 다이얼 

문제: 해당 단어에 맞춰 다이얼을 거는 최소 시간 구하기

input: 
알파벳 대문자로 이루어진 단어 (2 =< A =< 15)

output: 
최소시간 구하기 
"""
"""
TEST CASE 1: WA
OUTPUT 1: 13

TEST CASE 2: UNUCIC
OUTPUT 2: 36
"""
# input 받기
import sys 

input_case = input()

cal_time =[]
for alphabet in input_case: 
    if alphabet in ('A','B','C') :
        cal_time.append(3)
    elif alphabet in ('D', 'E', 'F'): 
        cal_time.append(4)
    elif alphabet in ('G', 'H','I'): 
        cal_time.append(5)
    elif alphabet in ('J', 'K' , 'L'): 
        cal_time.append(6)
    elif alphabet in ('M', 'N' , 'O'): 
        cal_time.append(7)
    elif alphabet in ('P' , 'Q' , 'R' , 'S'): 
        cal_time.append(8)
    elif alphabet in ('T' , 'U' , 'V'): 
        cal_time.append(9)
    elif alphabet in ('W' , 'X' , 'Y' , 'Z'):
        cal_time.append(10)

result = sum(cal_time)

print(result)
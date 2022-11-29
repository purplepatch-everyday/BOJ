"""
2914번: 저작권 

문제: 곡의 개수와 평균값이 주어졌을때 저작권이 있는 멜로디 개수 구하기
평균값은 올림이 된다
적어도 몇곡이 저작권이 있는 멜로디인지 출력해야한다. 
적어도...이기때문에 0.9999 float생각하기 

input: 앨범에 수록된 곡의 개수와 평균값


output: 저작권이 있는 멜로디 개수 구하기 
"""
# 올림을 하기 위해선 math를 import한다
import math

#input 받기 
input_num1, input_num2 = input().split()

avg = float(input_num2)-0.999999
result = int(input_num1) * avg
result_ceiling = math.ceil(result)

print(result_ceiling)

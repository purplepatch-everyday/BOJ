"""
2525번: 오븐시계 

문제: 시작하는 시간과 사용되는시간이 주어졌을때 끝날 시간 예측하기 

input: A B (시와분 공백으로 구분) (24시로 표시)
       C (사용되는 시간 0 <= C <= 1,000)

output: A B (끝나는 시간 출력, 시와 분 공백으로 구분)

"""
import sys

input_time = list(map(int,input().split()))

input_duration = int(input())

hour = input_duration//60
minute = input_duration%60

result_hour = input_time[0]+hour
result_min = input_time[1]+minute

if result_min>= 60:
    result_hour = result_hour+1
    result_min = result_min-60

if result_hour >= 24: 
    result_hour = result_hour-24
    
result= []
result.append(result_hour)
result.append(result_min)

print(*result)

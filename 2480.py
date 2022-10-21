"""
2480번: 주사위 세개 

문제: 규칙에 따라 상금을 받는다 

input: 주사위 3개에서 나올 숫자 (띄어쓰기로 구분)

output: 규칙에 따라 받을 상금 
"""

"""
규칙: 
A A A -> 10,000 + (A * 1000)
A A B -> 1,000 + (A * 100)
A B C -> max(A,B,C)*100

"""
import sys

input_dice = list(map(int,input().split()))

"""
set이라는 개념을 사용해 보자 
특징:
1. no duplicates (중복을 허용하지 않는다)
2. unordered (순서가 없다)


"""
check = set(input_dice)
num = len(check)

# 다 같을때 
if num == 1:
    value = 10000 + ((int(str(input_dice[0])))*1000)

elif num == 2:
    for i in input_dice:
        if input_dice.count(i) == 2:
            ans = i
    
    value = 1000 + ((ans)*100)
    
elif num == 3 :
    value = max(input_dice)*100
    
print(value)

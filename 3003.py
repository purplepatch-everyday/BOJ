# 체스 세트 맞추기 
# 킹 1, 퀸 1, 룩 2, 비숍 2, 나이트 2, 폰 8 

# input: 정리되지 않은 킹, 퀸, 룩, 비숍, 나이트, 폰
# output: 원하는 양만큼 계산하여 출력 
"""
Input_int 와 numchess에서 각 index 불러오기 
불러온 index 에서 연산 수행 (Input_int - numchess)
빈 리스트 (result)에 append
print result
"""

import sys


input_int = list(map(int,input().split()))

numchess = [1, 1, 2, 2, 2, 8]


result = []
for x, y in zip (numchess,input_int):
    result.append(x-y)

print(*result)
# print(type(result))
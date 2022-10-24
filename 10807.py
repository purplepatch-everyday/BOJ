"""
10807번: 개수 세기

문제: 정수와 문자열이 주어졌을때 해당 정수가 문자열 안에 몇개 있는지 출력하기

input: 
A - 정수 의 개수

B - 문자열로 주어진 정수 

C - 찾고자 하는 정수   

output: 찾은 정수가 몇개인지 출력

"""

"""
TEST CASE 1: 
11
1 4 1 2 4 2 4 2 3 4 4
2

OUTPUT 1: 3

################

TEST CASE 2: 
11
1 4 1 2 4 2 4 2 3 4 4
5

OUTPUT 2: 0 
"""

# input 받기
input_num = input()
input_list = input().split()
input_find = input()


result = 0 
# 리스트를 돌면서 해당 숫자가 있으면 답을 +1 한다
for num in input_list: 
    if input_find == num: 
        result+=1

print(result)
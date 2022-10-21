"""
25304번: 영수증 

문제: 영수증 총액이 실제 금액과 맞는지 확인하기 

input: 
A - 영수증에 적힌 총 금액 

B - 구매 종류의 수 

C D - 금액과 개수  

output: Yes, No - A의 금액과 C D 계산된 총액과 같으면 yes, 다르면 no 

"""

"""
TEST CASE 1: 
260000
4
20000 5
30000 2
10000 6
5000 8

OUTPUT 1: Yes

################

TEST CASE 2: 
250000
4
20000 5
30000 2
10000 6
5000 8

OUTPUT 2: No
"""

import sys 

# input A
input_total = int(input())
# input B
input_num = int(input())

# B만큼 돌아가면서 input 받기
price_total = []
for i in range (input_num): 
    input_price = list(map(int, input().split()))
    price_total.append(input_price[0]*input_price[1]) 
    # print("price total",price_total)

check_total = 0
for i in price_total:
    check_total += i
    # print("check total", check_total)

if input_total == check_total: 
    print("Yes")
else:
    print("No")
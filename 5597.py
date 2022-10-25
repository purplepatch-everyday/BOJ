"""
5597번: 과제 안 내신 분..? 

문제: 1-30 중 과제를 내지 않은 2명의 번호를 출력

input: 
28줄의 출석번호가 한줄씩 주어짐  

output: 28줄에 없는 2개의 번호 출력

"""
# input 받기 
# 28번의 input을 받아야 하기 때문에 while로 돌려 input을 받고 list애 추가한다.
# TIP: 작은 숫자로 먼저 코드가 작동하는지 확인해 보면 좋다. (예를들어 28 대신 5)

count = 0
num_list = []
while count < 28:
    input_num = input()
    num_list.append(int(input_num))
    count += 1

ori_list = list(range(1,31)) 

results = sorted(set(ori_list)- set(num_list))

for result in results: 
    print(result)

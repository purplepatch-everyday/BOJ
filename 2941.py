"""
2841번: 크로아티아 알파벳

문제: 알파벳과 기호로 이루어진 문자열에서 크로아티아 알파벳 개수로 출력하기

input: 
알파벳 소문자와 '-', '='로 이루어진 문자열

output: 
제시된 표에 맞추어 크로아티아식 알파벳 개수 출력하기 
"""
"""
TEST CASE 1: ljes=njak
OUTPUT 1: 6

TEST CASE 2: ddz=z=
OUTPUT 2: 3
"""
# input 받기
input_word = input()

# 크로아티아식 알파벳 표기 리스트
exceptions = ['c=','c-','dz=','d-','lj','nj','s=','z=']

index =-1 

word_count= len(input_word)

# 받은 input에서 exceptions를 찾으면 전체 input길이에서 하나씩 뺀다
# dz= 은 z=과 같이 찾아지기때문에 -2를 하지 않아도 결과 값이 -2로 계산 된다
for e in exceptions:
    while True:
        index = input_word.find(e,index+1)

        if(index != -1):
            word_count -= 1
        else:
            break

        # print(e, word_count)
print( word_count)
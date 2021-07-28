# BOJ 1065번: 한수  
# 함수를 이용한 문제 풀이 

# 함수 fuction(num)
def function(num):

    # 변수 만들기 -> 답
    result = 0 

    # 100이하 (두자리수 이하)의 한수는 자기 자신 만큼이 답
    if num < 100: 
        result = num
    # 100 이상 세자리 수 일때 
    else: 
        # 두자리수까지는 자기 자신 답이니 세자리 수 부터는 99까지 기본으로 더해준다.
        result = 99

        # 입력받은 값이 세자리 수 있때, 100 부터 입력받은 수 까지 loop 돌리기
        for i in range(100,num+1):
            # 데이터 값을 리스트로 변경
            num = list(map(int, str(i)))
            
            # 숫자의 첫째 자리수 와 둘째 자리수의 차이와 둘째자리와 셋째자리의 차이가 같다면 한수 이므로 결과에 1개 추가
            if num[0]-num[1] == num[1]-num[2]: 
                result +=1 

    # 함수는 답을 return 한다
    return result

# 실행하여 숫자를 입력 받음
num = int(input())

# function 함수 실행해서 함수의 답을 프린트
print(function(num))


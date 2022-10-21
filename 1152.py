"""
1152번: 단어의 개수

문제: 영어 대소문자와 공백으로 이루어진 문자열이 주어짐

input: 영어 대소문자로 이루어진 문자열 (단, 문자열의 앞과 뒤에 공백이 있을 수 있음)

output: 단어의 개수 출력 (단, 문자열 앞과 뒤에 있는 공백은 단어의 개수로 포함 X)
"""
"""
TEST CASE 1: The Curious Case of Benjamin Button
OUTPUT 1: 6

TEST CASE 2:  The first character is a blank
OUTPUT 2: 6

TEST CASE 3: The last character is a blank 
OUTPUT 3: 6
"""

#input 받기 
import sys

input_str = list(input().split())

print(len (input_str))

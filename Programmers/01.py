# 시저 암호 알고리즘 (https://school.programmers.co.kr/learn/courses/30/lessons/12926/solution_groups?language=python3&type=all)

# My code
def solution(s, n):
    # split 
    answer = ''
    text = list(s)
    for t in text:
        tta = ord(t)
        value = tta+n   
        if tta == 32:
            value = 32
        elif t.isupper() and value > 90:
            value = (value - 90) + 64
        elif value > 122:
            value = (value-122) + 96
        answer_str = chr(value)
        answer +=answer_str

    # 대문자인지 소문자인지 판단
    # 각각에 대해서 덧셈이 넘어가면 마이너스로 대문자는 90 , 소문자는 122까지

    return answer
 
# 다른 사람 풀이 (문자도 등호가 되는거 신기함)
def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer
  
def solution(s, n):
    return ''.join([chr(ord(i) + (not ord(i)==32)*((n%26) -26*((90<(ord(i)+(n%26))*(ord(i)<91)) + (122<(ord(i)+(n%26)))))) for i in s])

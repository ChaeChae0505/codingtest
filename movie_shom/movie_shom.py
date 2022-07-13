# 문제해석
## 666을 포함하는 숫자 중  N 번째를 찾으라는

N = int(input())
cnt = 0
six = 666

while cnt != N:
  
  if '666' in str(six):
    cnt +=1
    
  six+=1
print(six-1)

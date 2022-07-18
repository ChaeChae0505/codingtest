# N!의 값에서 0을 구하기 위해서는 5의 몫을 구하면 됨
# 근데 우리는 facotrial을 구해야하니깐!
# num = int(input())
# cnt = 0

# # N! 의 값
# while num >= 5:
#   cnt += num/5
#   num //=5
# print(int(cnt))


# 그게 아니라면 재귀함수를 사용해서 factorial을 구하고 str 변환 -> 0 세기
def factorial(n):
  return n*factorial(n-1) if n > 1 else 1

num = int(input())
cnt = 0
N = str(factorial(num))

for i in range(len(N)-1, -1, -1):
    if N[i] == '0':
        cnt += 1
    else:
        break
print(cnt)

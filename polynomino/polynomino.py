# 220712 무지하다,,,, 열심히 하자~!


board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)
    
"""
치환의 의미를 생각하자!
python  replace는 왼쪽부터 해당하는 문자열을 찾아서 치환해주는 함수라고 한다,,,,
다 치환 먼저 시켜버리고 안 된거는 X로 남아있을 것이니,,,, 하면 되는 거였는데!
나는 래와 같이 접근하고자 했다... 왜 replace를 생각할 수 없었을까,,,ㅎㅎㅎ 
반성~! ~! ~! replace~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!c++로는 내일한다 ! 
"""


rest = []
result_a = "AAAA"
result_b = "BB"

num = list(input())
rest_list = list(filter(lambda x: num[x] == '.', range(len(num))))
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

if len(rest_list) == 0:
  if len(num) % 2 !=0:
    print(-1)
  else:
    cal_a = len(num) / 4
    cal_b = len(num) % 4
    a = result_a*int(cal_a)
    b = result_b*int(cal_b)
    print(a+b)
else:
  if num[:rest_list[0]] % 2 !=0:
    print(-1)
  else:
    check = len(num[:rest_list[0]])
    cal_a = len(num) / 4
    cal_b = len(num) % 4
    a = result_a*int(cal_a)
    b = result_b*int(cal_b)
    rest.append(a+b)
    for x, y in zip(rest_list[1:], rest_list[2:]):
      check_x = num[x-1:y-1]
      cnt_x = check_x.count("X")
      if cnt_x % 2 !=0:
        print(-1)
      else:
        cnt_a = len(cnt_x) / 4
        cnt_b = len(cnt_x) % 4
        a = result_a*int(cnt_a)
        b = result_b*int(cnt_b)
        re = cnt_x.index(".")
        if re != 0:
          rest.append("."+a+b)
        else:
          rest.append(a+b)
      print(rest)
        
  

print(rest_list)

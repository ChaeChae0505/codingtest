
def findDecimal(x):
    for i in range(2, x):
        if x % i == 0:
            return
        
    return x
if __name__=="__main__":    
    num = input()
    number = map(int, input().split())
    result = []

    for i in number:
        if i !=1:
            x = findDecimal(i)
            result.append(x)


    result = [i for i in result if i is not None]
    cnt = len(result)
    print(cnt)

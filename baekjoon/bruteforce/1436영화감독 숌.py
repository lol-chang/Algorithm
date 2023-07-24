# https://www.acmicpc.net/problem/1436

N = int(input())
cnt = 0
x = 666

while True:
    #  if len(str(x).split('666')) >= 2:
    # ->
    if '666' in str(x): 
        cnt += 1
    if cnt == N:
        break
    x += 1    
print(x)
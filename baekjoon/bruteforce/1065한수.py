# https://www.acmicpc.net/problem/1065

x=int(input())
answer = 0 

for i in range(1,x+1):
    l=list(map(int,str(i)))
    if i < 100: 
        answer+=1
    elif l[0]-l[1] == l[1]-l[2]: 
        answer+=1

print(answer)
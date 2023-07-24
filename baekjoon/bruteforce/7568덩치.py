# https://www.acmicpc.net/problem/7568

x = int(input())
arr = []

for i in range(x):
    arr.append(list(map(int,input().split())))


for i in arr:
    k=1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            k+=1
    print(k, end=' ')

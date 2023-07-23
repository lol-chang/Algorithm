# https://www.acmicpc.net/problem/2231

x = int(input())

Isfind = False
for i in range(1, x+1):
    l = list(map(int, str(i)))
    if i + sum(l)==x:
        print(i)
        Isfind=True
        break

if not Isfind:
    print(0)
    
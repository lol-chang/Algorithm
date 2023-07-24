# https://www.acmicpc.net/problem/2798
import itertools

N, M = map(int, input().split())
x = list(map(int, input().split()))

l = list(itertools.combinations(x,3))

max =0
for i in l:
    if sum(i) <= M and sum(i)>max:
        max=sum(i)
print(max)
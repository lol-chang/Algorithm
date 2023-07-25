# https://www.acmicpc.net/problem/2309
import itertools

x = []
for _ in range(9):
    x.append(int(input()))

for i in itertools.combinations(x, 7):
    if sum(i)==100:
        res = sorted(i)
        for j in res:
            print(j)
        break

#이거를 c++로 한다면
# for문으로 돌려서 해야 하는데 
# 어떻게 하는지 잘 모르겠네 
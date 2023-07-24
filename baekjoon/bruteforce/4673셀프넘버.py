# https://www.acmicpc.net/problem/4673

x = []
for i in range(1, 10001):
    x.append(i+sum(list(map(int, str(i)))))

x.sort()
for i in range(1, 10001):
    if i not in x:
        print(i)


# 이렇게 짜는게 더 파이썬 코드 같네 
# n = set(range(1, 10001))
# res = sorted(list(n - x))

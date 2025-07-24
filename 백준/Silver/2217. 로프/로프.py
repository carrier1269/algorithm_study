import sys;input=sys.stdin.readline
lst = [];n=int(input())
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

rs = []
for i in range(n):
    rs.append(lst[i] * (i + 1))

print(max(rs))


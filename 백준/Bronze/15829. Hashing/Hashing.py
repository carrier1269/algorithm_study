import sys;input=sys.stdin.readline
n=int(input().strip())
char=input().strip();rs=0
for i in range(n):rs+=(ord(char[i])-96)*(31**i)
print(rs%1234567891)
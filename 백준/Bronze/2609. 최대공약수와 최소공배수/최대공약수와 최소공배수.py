import sys;import math;input=sys.stdin.readline
tmp_lst=list(map(int, input().rstrip().split()));a,b=tmp_lst[0],tmp_lst[1]
def gcd(a, b): return math.gcd(a, b)
def lcm(a, b): return a // gcd(a, b) * b
print(f"{gcd(a, b)}\n{lcm(a, b)}")
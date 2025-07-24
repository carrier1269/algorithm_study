import math;n=int(input());t=[]
l=list(map(int,input().split()));X = int(input())
def lcm(a, b):return a // math.gcd(a, b) * b
for i in l:
    if math.gcd(i, X) == 1 and lcm(i, X) == i * X:t.append(i)
print(sum(t)/len(t))
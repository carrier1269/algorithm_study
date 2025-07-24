n,c=int(input()),0
while n>=0:
    if n%5==0:print(c+n//5);break
    n-=3;c+=1
else:print(-1)
n = int(input())
def P(S,i,r,cnt):
    if(i>=r):return 1,cnt
    elif S[i]!=S[r]: return 0,cnt
    else:return P(S,i+1,r-1,cnt+1)
for _ in range(n):
    t=str(input().rstrip())
    print(*P(t,0,len(t)-1,1))
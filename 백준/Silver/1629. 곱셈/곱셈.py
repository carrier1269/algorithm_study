A,B,C=map(int,input().split())
def prime(a,b,c):
    if b==1:return a%c
    elif b==2:return (a*a)%c
    else:
        if b%2:return ((prime(a,b//2,c)**2)*a)%c
        else:return ((prime(a,b//2,c)**2))%c
print(prime(A,B,C))
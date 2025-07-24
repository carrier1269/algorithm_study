import sys;input=sys.stdin.readline
from itertools import permutations
while(True):
    try:
        A, B = map(str,input().rstrip().split())
        A = list(A)
        cnt = 0;st = False
        for i in permutations(A, len(A)):
            cnt += 1
            if cnt == int(B):
                print('{} {} = {}'.format(''.join(A), B, ''.join(i)));st = True;break
        if st:continue
        else:print('{} {} = No permutation'.format(''.join(A), B))
    except:break
from collections import deque
import sys
input=sys.stdin.readline; print=sys.stdout.write

N = int(input())
typeList = list(map(int, input().split()))
resultDataList = deque([x for idx, x in enumerate(map(int, input().split())) if typeList[idx] == 0])
numArrLength = int(input())
numArr = list(map(int, input().split()))

popDataTotal = list()

for num in numArr:
    # deque써서 반복문 안돌려도 됨
    resultDataList.appendleft(num)
    num = resultDataList.pop()

    popDataTotal.append(str(num))
print(' '.join(popDataTotal))
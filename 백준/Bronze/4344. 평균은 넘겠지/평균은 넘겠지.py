import sys;
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())

for _ in range(N):
    numList = list(map(int, input().split()))

    numSum = sum(numList[1:])
    numAverage = numSum / numList[0]

    overAverageCnt = [n for n in numList[1:] if n > numAverage]

    overAverageCnt = len(overAverageCnt)
    overAverageRate = float(format(100 / len(numList[1:]) * overAverageCnt, ".4f"))

    print(f"{overAverageRate:.3f}%\n")

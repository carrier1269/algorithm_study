import sys; input = sys.stdin.readline; print = sys.stdout.write
A, B, C = map(int, input().split(" "))
def algorithm(A, B, C):
    if (B >= C): return -1
    return A // (C - B) + 1
print(str(algorithm(A, B, C)))
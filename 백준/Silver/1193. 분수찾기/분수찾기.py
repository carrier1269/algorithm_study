import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

line = 1
while N > line: N -= line; line += 1

if line % 2 == 0: print(f"{N}/{line - N + 1}")
else: print(f"{line - N + 1}/{N}")
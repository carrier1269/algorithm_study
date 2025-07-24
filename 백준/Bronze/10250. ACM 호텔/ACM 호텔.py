import sys;input=sys.stdin.readline
n=int(input().strip())
for _ in range(n):
    lst = list(map(int, input().strip().split(" ")))
    if (lst[2] % lst[0] == 0): floor_num, room_num = lst[0], lst[2] // lst[0]
    else: floor_num, room_num = lst[2] % lst[0], lst[2] // lst[0] + 1
    if (len(str(room_num)) == 1): print(int(str(floor_num) + str(0) + str(room_num)))
    else: print(int(str(floor_num) + str(room_num)))

import sys;input=sys.stdin.readline
while True:
    input_list = list(map(int, input().strip().split()))
    if input_list == [0, 0, 0]: break
    input_list = sorted(input_list)
    if input_list[2]**2 != input_list[0]**2 + input_list[1]**2: print('wrong')
    else: print('right')
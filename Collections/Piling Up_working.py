from collections import deque

no_of_sets =int(input())

for i in range(no_of_sets):
    no_of_cubes = int(input())
    horizontal_cube = deque(map(int,input().split()))
    for side_length in reversed(sorted(horizontal_cube)):
        if horizontal_cube[0] == side_length:
            horizontal_cube.popleft()
        elif horizontal_cube[-1] == side_length:
            horizontal_cube.pop()
        else:
            print('No')
            break
    else:
        print('Yes')

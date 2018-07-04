no_of_sets = int(input())
from collections import deque

def formvertical_cube(h):
    if h:
        if not vertical_cube:
            if h[0] >= h[len(h)-1]:
                vertical_cube.append(h[0])
                horizontal_cube.popleft()
                formvertical_cube(horizontal_cube)
            else:
                vertical_cube.append(h[len(h)-1])
                horizontal_cube.pop()
                formvertical_cube(horizontal_cube)
        else:
            if vertical_cube[-1] >= h[0] and vertical_cube[-1] >= max(h) and h[0] >= h[len(h)-1]:
                vertical_cube.append(h[0])
                horizontal_cube.popleft()
                formvertical_cube(horizontal_cube)
            elif vertical_cube[-1] >= h[len(h)-1] and vertical_cube[-1] >= max(h) and h[len(h)-1] >= h[0]:
                vertical_cube.append(h[len(h)-1])
                horizontal_cube.pop()
                formvertical_cube(horizontal_cube)
        
for i in range(no_of_sets):
    vertical_cube = []
    no_of_cubes = int(input())
    horizontal_cube = deque(map(int,input().split()))
    #print(horizontal_cube)
    formvertical_cube(horizontal_cube)
    if len(vertical_cube) == no_of_cubes:
        print('Yes')
    else:
        print('No')
    #print(vertical_cube,horizontal_cube)

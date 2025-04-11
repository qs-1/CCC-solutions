curr = [0, 0]

max_x, max_y = map(int, input().strip().split())

while True:
    x, y = map(int, input().strip().split())

    if x == 0 and y == 0:
        break
    
    new_x = curr[0] + x
    new_y = curr[1] + y

    if new_x > max_x:
        curr[0] = max_x
    elif new_x < 0:
        curr[0] = 0
    else:
        curr[0] = new_x 

    if new_y > max_y:
        curr[1] = max_y
    elif new_y < 0:
        curr[1] = 0
    else:
        curr[1] = new_y 

    print(*curr)
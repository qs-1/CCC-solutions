import sys

x = int(input())
y = int(input())

if x == y:
    print(x)
    sys.exit()

# anticlockwise -> down, right, up, left
directions = [(1,0),(0,1),(-1,0),(0,-1)]
curr = [0,0] # start pos 
maze = {x:[0,0]} # start with the first already placed

num = x+1 # since placed first
direction = 0 # start going down
steps = 1 # for spiral, make 1 step down, 1 right then 2 up, 2 left and so on, +1 every 2 directions

while num <= y:
    for i in range(2): # same num of steps for 2 directions, then it increments by 1
            for j in range(steps): # in that direction, make 'steps' moves
                if num > y: # placed all
                        break
                curr[0] += directions[direction][0] # x coord for num
                curr[1] += directions[direction][1] # y coord
                maze[num] = curr[:] # make deepcopy
                num += 1 # next num
            direction = (direction + 1) % 4 #loop directions
    steps += 1 # completed 2 directions so increment steps

# find mins and maxes of nums positions to find dimensions needed for matrix
min_rows = min(x[0] for x in maze.values())
min_cols = min(x[1] for x in maze.values())
max_rows = max(x[0] for x in maze.values())
max_cols = max(x[1] for x in maze.values())

# find dimensions
# Add 1 because we need to find space required, not just distance between them
# for example, if we only have one number at [0,0], then max=0, min=0
# and we'd get  0-0 = 0, but we need atleast 1 row to place the num
rows = max_rows - min_rows + 1 
cols = max_cols - min_cols + 1

#make the 2d matrix for placing nums
spiral = [["  "]*cols for i in range(rows)]

# place the nums (while fixing negative indexes by adding ABS of largest negative)
for num, pos in maze.items():
    x_pos = pos[0] - min_rows # same as + abs(-ive)
    y_pos = pos[1] - min_cols
    
    spiral[x_pos][y_pos] = num

# print the final spiral
for row in spiral:
    print(*row)

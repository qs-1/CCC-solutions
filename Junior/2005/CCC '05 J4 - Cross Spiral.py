x = int(input())
y = int(input())
cx = int(input())
cy = int(input())
steps = int(input()) 

# make the grid for the house and mark cutouts with -1
grid = [[0]*x for _ in range(y)]

for i in range(cy):
    for j in range(cx):
        grid[i][j] = -1 # top left corner
        grid[i][x-j-1] = -1 # top right
        grid[y-i-1][j] = -1 # bottom left
        grid[y-i-1][x-j-1] = -1 # bottom right

# order of priority for each direction,
priorities = {
    "right": ["up", "right", "down"], 
    "down": ["right", "down", "left"],
    "left": ["down", "left", "up"],
    "up": ["left", "up", "right"]
}

# pos change mapping for move
directions = {
    "right": [0, 1],
    "down": [1, 0],
    "left": [0, -1],
    "up": [-1, 0]
}

curr = [0,cx] # start in top left empty pos, thats to the right of topleft cutout
grid[curr[0]][curr[1]] = -1 # mark start as visited
prev = 'right'

for i in range(steps):
    stuck = 0
    for move in priorities[prev]:
        #check if move valid, if yes the make it the new prev
        new = [curr[0]+directions[move][0], curr[1]+directions[move][1]] # find the pos after making move in that direction

        #check if valid,    rows                                cols                            not visited
        if new[0] >= 0 and new[0] < len(grid)  and  new[1] >= 0 and new[1]<len(grid[0])  and  grid[new[0]][new[1]] != -1:
            grid[new[0]][new[1]] = -1 # mark visietd
            curr = new[:] # update position
            prev = move # update prev move for next iteration
            break

        stuck += 1

    if stuck == 3: #checked all possible moves at current, none valid so we're stuck
        break

# make both 1 indexed
print(curr[1]+1) # col
print(curr[0]+1) # row










# longer no loop version, copy pasting after writing one if block, just order different
x = int(input())
y = int(input())
cx = int(input())
cy = int(input())
steps = int(input()) 

grid = [[0]*x for _ in range(y)]

for i in range(cy):
    for j in range(cx):
        grid[i][j] = -1 # top left corner
        grid[i][x-j-1] = -1 # top right
        grid[y-i-1][j] = -1 # bottom left
        grid[y-i-1][x-j-1] = -1 # bottom right

curr = [0,cx]
grid[curr[0]][curr[1]] = -1
prev = 'right'

for i in range(steps):
    before = curr[:]
    if prev == 'right':
        if curr[0]-1 >= 0 and grid[curr[0]-1][curr[1]] != -1:
            prev = 'up'
            curr = [curr[0]-1, curr[1]]
            grid[curr[0]][curr[1]] = -1

        elif curr[1]+1 < len(grid[0]) and grid[curr[0]][curr[1]+1] != -1:
            prev = 'right'
            curr = [curr[0], curr[1]+1]
            grid[curr[0]][curr[1]] = -1

        elif curr[0]+1 < len(grid) and grid[curr[0]+1][curr[1]] != -1:
            prev = 'down'
            curr = [curr[0]+1, curr[1]]
            grid[curr[0]][curr[1]] = -1

    elif prev == 'down':
        if curr[1]+1 < len(grid[0]) and grid[curr[0]][curr[1]+1] != -1:
            prev = 'right'
            curr = [curr[0], curr[1]+1]
            grid[curr[0]][curr[1]] = -1

        elif curr[0]+1 < len(grid) and grid[curr[0]+1][curr[1]] != -1:
            prev = 'down'
            curr = [curr[0]+1, curr[1]]
            grid[curr[0]][curr[1]] = -1

        elif curr[1]-1 >= 0 and grid[curr[0]][curr[1]-1] != -1:
            prev = 'left'
            curr = [curr[0], curr[1]-1]
            grid[curr[0]][curr[1]] = -1

    elif prev == 'left':
        if curr[0]+1 < len(grid) and grid[curr[0]+1][curr[1]] != -1:
            prev = 'down'
            curr = [curr[0]+1, curr[1]]
            grid[curr[0]][curr[1]] = -1

        elif curr[1]-1 >= 0 and grid[curr[0]][curr[1]-1] != -1:
            prev = 'left'
            curr = [curr[0], curr[1]-1]
            grid[curr[0]][curr[1]] = -1

        elif curr[0]-1 >= 0 and grid[curr[0]-1][curr[1]] != -1:
            prev = 'up'
            curr = [curr[0]-1, curr[1]]
            grid[curr[0]][curr[1]] = -1

    elif prev == 'up':
        if curr[1]-1 >= 0 and grid[curr[0]][curr[1]-1] != -1:
            prev = 'left'
            curr = [curr[0], curr[1]-1]
            grid[curr[0]][curr[1]] = -1
        
        elif curr[0]-1 >= 0 and grid[curr[0]-1][curr[1]] != -1:
            prev = 'up'
            curr = [curr[0]-1, curr[1]]
            grid[curr[0]][curr[1]] = -1
        
        elif curr[1]+1 < len(grid[0]) and grid[curr[0]][curr[1]+1] != -1:
            prev = 'right'
            curr = [curr[0], curr[1]+1]
            grid[curr[0]][curr[1]] = -1
    if before == curr:
        break
print(curr[1]+1)
print(curr[0]+1)

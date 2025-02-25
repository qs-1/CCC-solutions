# 9/15 score on dmoj, TLE on last 2 cases
# running simulation for each cell and marking end if no obstacle encountered in poth
# r = int(input())
# c = int(input())

# maze = []
# for i in range(r):
#     maze.append(list(input().strip()))

# m = int(input())

# moves = []
# for i in range(m):
#     moves.append(input().strip())

# # Correct directions: North: row -1, South: row +1, East: col +1, West: col -1
# directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

# # Define right and left turns
# right_turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
# left_turn = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

# for i in range(r):
#     for j in range(c):
#         if maze[i][j] != 'X':
#             for facing in directions:  # try all starting headings
#                 curr = [i, j]
#                 current_facing = facing
#                 valid = True


#                 for move in moves:

#                     if move == 'F':
#                         curr[0] += directions[current_facing][0]
#                         curr[1] += directions[current_facing][1]
#                         if not (0 <= curr[0] < r and 0 <= curr[1] < c) or maze[curr[0]][curr[1]] == 'X':
#                             valid = False
#                             break

#                     elif move == 'R':
#                         current_facing = right_turn[current_facing]

#                     elif move == 'L':
#                         current_facing = left_turn[current_facing]

#                 if valid:
#                     maze[curr[0]][curr[1]] = '*'

# for row in maze:
#     print("".join(row))




# 15/15 on dmoj, precalculating offset paths for all 4 directions once
# and only checking unique cells in the path
r = int(input())
c = int(input())

maze = []
for i in range(r):
    maze.append(list(input().strip()))

m = int(input())

moves = []
for i in range(m):
    moves.append(input().strip())

directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

right_turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
left_turn = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

def path(facing):
    unique_cells = set()

    curr = [0,0]
    unique_cells.add(tuple(curr))
    length = len(moves)

    for i in range(length):
        move = moves[i]

        if move == 'F':
            curr[0] += directions[facing][0]
            curr[1] += directions[facing][1]
        
            if i == length - 1: 
                end = curr[:]
            unique_cells.add(tuple(curr[:]))
            
        elif move == 'R':
            facing = right_turn[facing]
        
        elif move == 'L':
            facing = left_turn[facing]
    
    end = curr[:]
    return end, unique_cells

"""
Using the observation that the path itself wont change for each direction, it will just shift
depending on where the path begins, for example if offets path is:
      . (0,0)
      |
(1,0) .__. (1,1)

Then using this we can find the path for any starting position, if started at 2,3
then we would just add 2 to each offsets x coordinate and similarly 3 to y coord

      . (2,3)
      |
(3,3) .__. (3,4)

This way we dont need to run the path simulation for each cell all over again
"""

relative_ends = {} # need to store the ending position for each direction separately since order is not maintained in set
unique_offsets = {} # will store offsets path for each direction in a set to not repeat checks for cells
for direction in directions:
    relative_ends[direction], unique_offsets[direction] = path(direction)

for i in range(r):
    for j in range(c):
        if maze[i][j] != 'X': 

            for direction in  directions: # iterate over 4 directions paths NSEW (only unique cells so we dont repeat validity checks)
                unique_offset = unique_offsets[direction] 
                end = relative_ends[direction]
                valid = True

                for curr in unique_offset: #check if cells in path are valid (none blocked i.e. 'X', and within bounds)
                    
                    if not ( 0 <= i+curr[0] < r and 0 <= j+curr[1] < c and maze[i+curr[0]][j+curr[1]] != 'X' ):
                        valid = False
                        break
                
                # went through all cells in current path and all valid, mark the end 
                if valid:
                    maze[end[0]+i][end[1]+j] = '*'

for row in maze:
    print("".join(row))

r = int(input())
c = int(input())

maze = []
for i in range(r):
    maze.append(list(input().strip()))

m = int(input())

moves = []
for i in range(m):
    moves.append(input().strip())

# North: row -1, South: row +1, East: col +1, West: col -1
directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

#  right and left turns
right_turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
left_turn = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

for i in range(r):
    for j in range(c):
        if maze[i][j] != 'X':
            for facing in directions:  # try all 4 possibles directions colin may be facing in the start
                curr = [i, j]
                current_facing = facing
                valid = True

                for move in moves:
                    if move == 'F':
                        curr[0] += directions[current_facing][0]
                        curr[1] += directions[current_facing][1]
                        if not (0 <= curr[0] < r and 0 <= curr[1] < c) or maze[curr[0]][curr[1]] == 'X':
                            valid = False
                            break
                    elif move == 'R':
                        current_facing = right_turn[current_facing]
                    elif move == 'L':
                        current_facing = left_turn[current_facing]

                if valid:
                    maze[curr[0]][curr[1]] = '*'

for row in maze:
    print("".join(row))

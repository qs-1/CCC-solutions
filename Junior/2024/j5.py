rows = int(input())
cols = int(input())

maze = []
for i in range(rows):
    maze.append(list(input().strip()))

start_row = int(input())
start_col = int(input())

from collections import deque
def bfs(start,rows,cols,maze):
    queue = deque()
    queue.append(start)
    visited = set()
    moves = [(1,0),(0,1),(-1,0),(0,-1)]

    value = {
        'S':1,
        'M':5,
        'L':10
    }

    dollars = 0

    while queue:
        curr = queue.popleft()
        visited.add(curr)
        pumpkin = maze[curr[0]][curr[1]]
        dollars += value[pumpkin]

        for move in moves:
            new = (curr[0]+move[0], curr[1]+move[1])

            if new[0] >= 0 and new[0] < rows and new[1] >= 0 and new[1] < cols:
                if maze[new[0]][new[1]] != '*':
                    if new not in visited:
                        queue.append(new)
                        visited.add(new)
    return dollars

print(bfs((start_row,start_col),rows,cols,maze))
"""Problem Description
You have to determine if it is possible to escape from a room. The room is an M -by-N grid with
each position (cell) containing a positive integer. The rows are numbered 1, 2, . . . , M and the
columns are numbered 1, 2, . . . , N . We use (r, c) to refer to the cell in row r and column c.
You start in the top-left corner at (1, 1) and exit from the bottom-right corner at (M, N ). If you
are in a cell containing the value x, then you can jump to any cell (a, b) satisfying a ×b = x. For
example, if you are in a cell containing a 6, you can jump to cell (2, 3).
Note that from a cell containing a 6, there are up to four cells you can jump to: (2, 3), (3, 2), (1, 6),
or (6, 1). If the room is a 5-by-6 grid, there isn’t a row 6 so only the first three jumps would be
possible.
Input Specification
The first line of the input will be an integer M (1 ≤M ≤1000). The second line of the input will
be an integer N (1 ≤N ≤1000). The remaining input gives the positive integers in the cells of
the room with M rows and N columns. It consists of M lines where each line contains N positive
integers, each less than or equal to 1 000 000, separated by single spaces.
For 1 of the 15 available marks, M = 2 and N = 2.
For an additional 2 of the 15 available marks, M = 1.
For an additional 4 of the 15 available marks, all of the integers in the cells will be unique.
For an additional 4 of the 15 available marks, M ≤200 and N ≤200.
Output Specification
Output yes if it is possible to escape from the room. Otherwise, output no.
Sample Input
3
4
3 10 8 14
1 11 12 12
6 2 3 9
Output for Sample Input
yes"""
from collections import deque
from math import isqrt

rows = int(input())
cols = int(input())

maze = []
pairs = {} 

for i in range(rows):
    row = list(map(int, input().split()))
    maze.append(row)

    for num in row:
        if num not in pairs:
            moves = []

            for k in range(1, isqrt(num) + 1):
                if num % k == 0:
                    a = k
                    b = num // a

                    if a <= rows and b <= cols:
                        moves.append((a - 1, b - 1))
                
                    if a != b and b <= rows and a <= cols:
                        moves.append((b - 1, a - 1))
           
            pairs[num] = moves


def bfs(M, N):
    queue = deque()
    visited = [[False] * cols for _ in range(rows)]
    
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        r, c = queue.popleft()
        
        # found the exit
        if (r, c) == (M-1, N-1):
            return True
        
        num = maze[r][c]
        for nr, nc in pairs[num]:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))
    return False

print('yes' if bfs(rows, cols) else 'no')

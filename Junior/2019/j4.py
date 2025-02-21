grid = [
    [1,2],
    [3,4]
]

operations = input()

v_count = operations.count('V')
h_count = operations.count('H')

if v_count%2 != 0: # swap columns
    grid[0][0], grid[1][0], grid[0][1], grid[1][1] = grid[0][1], grid[1][1], grid[0][0], grid[1][0]
    
if h_count%2 != 0:
    grid[0], grid[1] = grid[1], grid[0]

for i in range(2):
    for j in range(2):
        print(grid[i][j],end=" ")

    print()
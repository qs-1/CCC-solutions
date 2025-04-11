def check_winner(move):
    #check rows
    for j in range(3):
        if grid[j][0] == move and grid[j][0] == grid[j][1] == grid[j][2]:
            return True

    #check cols
    for k in range(3):
        if grid[0][k] == move and grid[0][k] == grid[1][k] == grid[2][k]:
            return True

    #check diags (\ and /)
    if grid[0][0] == move and grid[0][0] == grid[1][1] == grid[2][2]:
        return True
    if grid[0][2] == move and grid[0][2] == grid[1][1] == grid[2][0]:
        return True



cases = int(input())

for i in range(cases):
    s = input()

    # O moves cant be more than X, also, X cant be more than 1 move ahead of O
    if s.count('O') > s.count('X') or (s.count('X') - s.count('O')) > 1:
        print('no')
        continue

    grid = [
        ['','',''],
        ['','',''],
        ['','','']
    ]

    # fill grid
    move_idx = 0
    for row in range(3):
        for col in range(3):
            grid[row][col] = s[move_idx]
            move_idx += 1

    # check if both X and O won (impossible)
    if check_winner('X') and check_winner('O'):
        print('no')
        continue

    # if X won, must have one more X than O
    if check_winner('X') and s.count('X') - s.count('O') != 1:
        print('no')
        continue

    # if O won, must have equal X and O
    if check_winner('O') and s.count('X') - s.count('O') != 0:
        print('no')
        continue

    # valid otherwise
    print('yes')
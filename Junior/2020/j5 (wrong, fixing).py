"""Problem J5/S2: Escape Room
Problem Description
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
yes
La version franc ̧aise figure `a la suite de la version anglaise.
Explanation of Output for Sample Input
Starting in the cell at (1, 1) which contains a 3, one possibility is to jump to the cell at (1, 3).
This cell contains an 8 so from it, you could jump to the cell at (2, 4). This brings you to a cell
containing 12 from which you can jump to the exit at (3, 4). Note that another way to escape is to
jump from the starting cell to the cell at (3, 1) to the cell at (2, 3) to the exit"""

rows = int(input())
cols = int(input())

maze = []
for _ in range(rows):
    maze.append(list(map(int, input().split())))

from math import sqrt
def dfs(M,N,maze):
    pairs = {}
    for i in range(M):
        for j in range(N):
            num = maze[i][j]

            #make all possible a,b pairs that satisfy a*b = x
            if num not in pairs:
                pairs[num] = []

                #min() so k is within bounds and + 1 to include the sqrt itself or M itself
                for k in range(1, min( int(sqrt(num)), M) + 1): #a cant be more than number of rows, also cant be more than the number itself
                    if num%k == 0: #check which number is a factor of num 
                        #a is k, b is quotient
                        b = num//k
                        #also ensure b is not more than number of columns
                        if b <= N:
                            pairs[num].append((k,b))
    
    #traverse every possible path for each index starting from 1,1
    memo = {}
    def helper(curr):
        if curr in memo:
            return memo[curr]

        if curr == (M,N):
            return True
        
        found = False 
        num = maze[curr[0]-1][curr[1]-1] #-1 since its 1 indexed

        #search all possible moves from current index
        for move in pairs[num]:
            found = helper(move)
            if found: #found the path that leads to M,N so just return True here
                return found
        
        memo[curr] = found
        return False
    
    return helper((1,1))

print('yes' if dfs(rows,cols,maze) else 'no')









"""

1
200
142 125 103 110 162 192 10 115 8 182 61 170 171 80 15 74 44 88 59 51 96 147 48 114 194 149 141 47 34 130 2 144 12 58 27 131 33 25 124 20 18 105 37 81 55 132 136 137 46 84 69 200 111 135 60 186 45 9 123 181 21 63 92 13 187 189 72 35 85 67 68 176 73 173 94 195 175 32 90 160 152 95 62 76 146 139 117 104 99 116 24 128 71 129 158 106 151 179 29 164 75 145 138 107 133 16 4 112 38 89 191 198 101 155 185 49 86 184 188 118 7 52 39 36 43 108 167 134 196 56 19 109 140 177 82 154 50 97 23 197 77 102 53 199 120 83 93 113 169 91 126 122 30 57 65 31 17 3 161 174 78 193 172 54 157 127 41 28 64 121 156 159 26 70 42 119 180 100 98 150 66 22 79 178 153 40 1 148 14 183 166 11 6 165 190 168 163 5 87 143

output: yes
"""
def solve(x,y):
      if x == y:
            print(x)
            return

      directions = [(1,0),(0,1),(-1,0),(0,-1)]
      curr = [0,0]

      #down
      #right
      #up
      #down

      maze = {x:[0,0]} #start with already placing the first

      num = x+1 #since placed first
      steps = 1 #same thing here
      direction = 0 #start at down direction

      while num <= y:
            for i in range(2):
                  for j in range(steps): #move in the direction 'steps' number of times
                        if num > y: #stop when all placed (y inclusive)
                              break
                        curr[0] += directions[direction][0]
                        curr[1] += directions[direction][1]
                        maze[num] = [curr[0], curr[1]] 
                        num += 1

                  direction = (direction + 1) % 4 #wraps around
            steps += 1

      # find mins and maxes for finding dimensions of matrix
      min_rows = min(x[0] for x in maze.values())
      min_cols = min(x[1] for x in maze.values())
      max_rows = max(x[0] for x in maze.values())
      max_cols = max(x[1] for x in maze.values())

      # find dimensions
      rows = max_rows - min_rows + 1 # need +1 since we need to include the ending too, otherwise we only count the gap between. for example when min max = 2 then 2-2 = 0 rows but it should be 1 row
      cols = max_cols - min_cols + 1

      #make the 2d matrix for placing nums
      spiral = [["  "]*cols for i in range(rows)]

      # place the nums (while fixing negative indexes by adding ABS of largest negative, this would make them all non negative)
      for num, pos in maze.items():
            x = pos[0] - min_rows
            y = pos[1] - min_cols
            
            spiral[x][y] = num

      # print the final spiral
      for row in spiral:
            print(*row)

x = int(input())
y = int(input())

solve(x,y)
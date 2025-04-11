n = int(input())

min_x = float('inf')
min_y = float('inf')

max_x = -float('inf')
max_y = -float('inf')

for i in range(n):
    x, y = map(int, input().split(','))
    
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    
    max_x = max(max_x, x)
    max_y = max(max_y, y)

print(f"{min_x-1},{min_y-1}")
print(f"{max_x+1},{max_y+1}")

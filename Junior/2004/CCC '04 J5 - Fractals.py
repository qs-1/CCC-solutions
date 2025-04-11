lvl, width, at_x = map(int, input().split())
lines = {
    ((0, 1), (width, 1)): 'U'
}

for i in range(lvl):
    # because fractal lines at each level become 1/3 of the previous level
    # 27/3 = 9 then 27/9 = 3 then 27/27 = 1 lengths for each segment
    # square 3 at each step and divide
    DI = width // (3**(i+1)) 

    new_lines = {}
    for (p1, p2), bump in lines.items():
        # find the bottom point for vertical or left point for horiztonal
        # to use for indexing new segments
        x = min(p1[0], p2[0]) 
        y = min(p1[1], p2[1])
            
        if bump == 'U': # before ___
            new_lines[((x, y), (x+DI, y))] = 'U' #first half _ 
            new_lines[((x+DI, y), (x+DI, y+DI))] = 'L'
            new_lines[((x+DI, y+DI), (x+2*DI, y+DI))] = 'U' # << middle bump up
            new_lines[((x+2*DI, y+DI), (x+2*DI, y))] = 'R'
            new_lines[((x+2*DI, y), (x+3*DI, y))] = 'U' # last half _
        elif bump == 'D':
            new_lines[((x, y), (x+DI, y))] = 'D'
            new_lines[((x+DI, y), (x+DI, y-DI))] = 'L'
            new_lines[((x+DI, y-DI), (x+2*DI, y-DI))] = 'D'
            new_lines[((x+2*DI, y-DI), (x+2*DI, y))] = 'R'
            new_lines[((x+2*DI, y), (x+3*DI, y))] = 'D'
        elif bump == 'L':
            new_lines[((x, y), (x, y+DI))] = 'L'
            new_lines[((x, y+DI), (x-DI, y+DI))] = 'D'
            new_lines[((x-DI, y+DI), (x-DI, y+2*DI))] = 'L'
            new_lines[((x-DI, y+2*DI), (x, y+2*DI))] = 'U'
            new_lines[((x, y+2*DI), (x, y+3*DI))] = 'L'
        elif bump == 'R':
            new_lines[((x, y), (x, y+DI))] = 'R'
            new_lines[((x, y+DI), (x+DI, y+DI))] = 'D'
            new_lines[((x+DI, y+DI), (x+DI, y+2*DI))] = 'R'
            new_lines[((x+DI, y+2*DI), (x, y+2*DI))] = 'U'
            new_lines[((x, y+2*DI), (x, y+3*DI))] = 'R'
    lines = new_lines

cuts = set()
for p1, p2 in lines:
    a, b = sorted([p1, p2])
    if a[0] == b[0] == at_x: #vertical line, every point is overlapping so add those ys
        for j in range(a[1], b[1] + 1):
            cuts.add(j)
    elif a[1] == b[1] and a[0] <= at_x <= b[0]: # horizontal, only add y when x lies on point
        cuts.add(a[1])
print(*sorted(cuts))
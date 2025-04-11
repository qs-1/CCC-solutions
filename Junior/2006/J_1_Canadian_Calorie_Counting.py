menu = [461, 431, 420, 0,
    100, 57, 70, 0,
    130, 160, 118, 0,
    167, 266, 75, 0]

cal = 0
for i in range(4):
    n = int(input())
    x = i*4 + n-1
    cal += menu[x]

print(f"Your total Calorie count is {cal}.")
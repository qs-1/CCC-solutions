cell = {}
groups = {}

group_num = 0
press_count = 0

# mapping for letters on a phone keypad (key presses needed and which group it belongs to)
for i in range(26):
    press_count += 1
    letter = chr(97 + i)
    groups[letter] = group_num  # which keypad group the letter belongs to
    cell[letter] = press_count  # number of presses needed for this letter

    # reset press_count and group_num after 3 presses, except for letters 'r' and 'y' as that group has 4 letters
    if letter not in ('r', 'y') and press_count >= 3:
        press_count = 0
        group_num += 1

while True:
    s = input()

    if s == 'halt':
        break
    
    if not s:
        print(0)
        continue

    # find time needed by adding key presses needed for each char,
    # and if consecutive chars on same button, add timeout
    cnt = cell[s[0]]

    for i in range(1,len(s)):
        if groups[s[i]] == groups[s[i-1]]: # same button, need to wait 2 secs
            cnt += 2

        cnt += cell[s[i]] # 1 second to press it

    print(cnt)
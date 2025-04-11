s = input()

hap = 0
sad = 0

for i in range(len(s)-2):
    if s[i:i+3] == ':-(':
        sad += 1

    elif s[i:i+3] == ':-)':
        hap += 1

if not (hap or sad):
    print('none')

elif hap == sad:
    print('unsure')

elif hap>sad:
    print('happy')

else:
    print('sad')
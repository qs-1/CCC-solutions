snakes = {54:19,90:48,99:77}

ladders = {9:34,40:64,67:86}

curr = 1

while True:
    dice = int(input())

    if dice == 0:
        print("You Quit!")
        break

    if not curr + dice > 100:
        curr += dice
    
    if curr == 100:
        print(f'You are now on square {curr}')
        print('You Win!')
        break

    if curr in snakes:
        curr = snakes[curr]

    elif curr in ladders:
        curr = ladders[curr]

    print(f'You are now on square {curr}')





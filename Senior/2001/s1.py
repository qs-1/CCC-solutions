suits = input()

C = ""
D = ""
H = ""
S = ""

i = 0

while suits[i] != "D":
    C += suits[i]
    i+=1


while suits[i] != "H":
    D += suits[i]
    i+=1

while suits[i] != "S":
    H += suits[i]
    i+=1

S = suits[i:]

# print(C)
# print(D)
# print(H)
# print(S)

mapping = {"C":"Clubs","D":"Diamonds","H":"Hearts","S":"Spades"}

print("Cards Dealt  Points")

# points for clubs
def scores(hand):
    points = 0
    cards = hand[1:]
    
    if len(cards) == 0:
        points = 3

    else:
        if len(cards) == 1:
            points = 2
        elif len(cards) == 2:
            points = 1

        points += cards.count("A")*4

        points += cards.count("K")*3

        points += cards.count("Q")*2

        points += cards.count("J")*1

    print(f"{mapping[hand[0]]}",end=" ")
    print(*hand[1:], end = ' ')
    print(points)

    return points

total = 0
total += scores(C)
total += scores(D)
total += scores(H)
total += scores(S)

print(f"             Total {total}")

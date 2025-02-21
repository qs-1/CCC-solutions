import math
x = int(input())
y = int(input())

R = x%y
Q = x//y

if R == 0:
    print(Q)

else:
    D = y

    #check if we can simpify R/D, divide by common factor
    common = math.gcd(R,D)
    R = R//common
    D = D//common
    
    #check if its an improper fraction
    if x>y:
        print(f"{Q} {R}/{D}")

    else: #it is a proper fraction eg 3/10 so Q would be 0
        print(f"{R}/{D}")
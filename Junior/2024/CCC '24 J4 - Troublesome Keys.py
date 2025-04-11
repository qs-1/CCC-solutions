import sys
org = input()
mess = input()

mess_set = set(mess)
org_set = set(org)

silly = list(mess_set.difference(org_set))[0]

if len(org) == 1:
    print(org[0], silly)
    print('-')
    sys.exit()

if len(org) == 2:
    print(org[0] if org[0] != mess[0] else org[1], silly)
    print('-')
    sys.exit()

#otherwise it may have a quiet key for len >= 3
quiet = '-'
silly_original = None

for i in range(len(org)):
    if org[i] != mess[i]:
        if mess[i] == silly: # found silly original
            silly_original = org[i]

            # now find the quiet key only if it was pressed
            if len(org) != len(mess):
                # fix the silly key and use set difference to get the quiet
                mess_set.remove(silly)
                mess_set.add(silly_original)
                quiet = list(org_set.difference(mess_set))[0]

        else: # found quiet key
            quiet = org[i]

            # add back quiet and use set difference to get silly
            mess_set.add(quiet)
            silly_original = list(org_set.difference(mess_set))[0]

        break # break in both cases since we found the original of silly and quiet in one mismatch

print(silly_original, silly)
print(quiet)







###    version 2
original = input()
messed = input()

silly_messed = list(set(messed).difference(set(original)))[0]

olen = len(original)
mlen = len(messed)

if olen == 1:
    print(original[0], silly_messed)
    print('-')

elif olen == 2 or olen == mlen:
    for i in range(olen):
        if original[i] != messed[i]:
            print(original[i], silly_messed)
            print('-')
            break

else: # means theres a quiet key smallest form = silly X quiet 
    for i in range(mlen):
        if original[i] != messed[i]:
            a,b = set(original).difference(set(messed))

            if messed[i] == silly_messed: # found original silly
                print(original[i], silly_messed)
                print(a if a != original[i] else b)
                break
            
            else: # found the quiet
                print(a if a != original[i] else b, silly_messed)
                print(original[i])
                break


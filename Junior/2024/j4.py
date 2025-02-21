original = 'forloops'
messed = 'frlpz'

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


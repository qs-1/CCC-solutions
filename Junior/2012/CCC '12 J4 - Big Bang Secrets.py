def shift_amount(p, k):
    return 3*p + k

k = int(input())
s = input()

for i in range(len(s)):
    c = s[i]

    # we are decoding, so need we'll need to revert the prev shift done forward
    # subtract to do that, going backwards basically
    shift = (ord(c) - ord('A')) - shift_amount(i+1, k)

    # shift may be positive or negative
    # also, we need to wrap around the alphabet
        # this wraparound modulo also handles the negative case
        # since modulo of a negative number here gives the
        # remainder after subtracting from 26
        # eg -1 % 26 = 25 which is Z 
    shift = shift % 26

    print(chr(shift + ord('A')), end='')

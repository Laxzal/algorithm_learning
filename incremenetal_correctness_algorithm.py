'''

Problem: Prove the correctness of the following recursive algorithm for incre- menting natural numbers, that is, y → y + 1:
Increment(y)
if (y = 0) then return(1) else
if (y mod 2) = 1 then
return(2 · Increment(⌊y/2⌋))
else return(y + 1)

'''
import math


def incr_correct(y):
    if y == 0:
        return 1
    else:
        if y%2 == 1:
            return 2*incr_correct(math.floor(y/2))
        else:
            return (y+1)


print(incr_correct(11))
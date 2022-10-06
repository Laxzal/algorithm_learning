'''

Shift method

c is the base and must be bigger than or equal to 2 - c>= 2

When c is the base of your representation (like decimal), then this is how multiplication can be done "manually".
It's the "shift and add" method. In c-base cy is a single shift of y to the left (i.e. adding a zero at the right);
and z/c is a single shift of z to the right: the right most digit is lost. That lost digit is actually z mod c,
which is multiplied with y separately.

Here is an example with c = 10, where the apostrophe signifies the value of variables in a recursive call. We perform
the multiplication with y for each separate digit of z (retrieved with z mod c). Each next product found in this way
is written shifted one more place to the left. Usually the 0 is not padded at the right of this shifted product,
but it is silently assumed:

'''
import math


def multiply(y, z, c):
    if z == 0 or y == 0:
        return 0
    else:
        return multiply(c * y, math.floor((z / c)), c) + y * (z % c)


print(multiply(10, 20, 2))

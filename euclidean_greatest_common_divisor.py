'''
gcd(a,b,c)=gcd(gcd(a,b),c)


 Determine the greatest common factor of 84 and 132.

We follow our algorithm:

    aaa is 84 and bbb is 132. Since b>ab > ab>a, we replace bbb with b−a=132−84=48b - a = 132 - 84 = 48b−a=132−84=48.
    aaa is 84 and bbb is 48. Since a>ba > ba>b, we replace aaa with a−b=84−48=36a - b = 84 - 48 = 36a−b=84−48=36.
    aaa is 36 and bbb is 48. Since b>ab > ab>a, we replace bbb with b−a=12b - a = 12b−a=12.
    aaa is 36 and bbb is 12. Since a>ba > ba>b, we replace aaa with a−b=24a - b = 24a−b=24.
    aaa is 24 and bbb is 12. Since a>ba > ba>b, we replace aaa with a−b=12a - b = 12a−b=12.
    aaa is 12 and bbb is 12. Since a=ba = ba=b, the GCD is 12.



'''

# 132, 84

a = 84
b = 132


##for two values only
def greatest_common_divisor_two_values(a, b):
    while a != b:
        if b > a:
            b = b - a
        elif a > b:
            a = a - b
    return a


# 20, 28, and 24,
a = 30
b = 3000
c = 10


def greatest_common_divisor_three_values(a, b, c):
    z = greatest_common_divisor_two_values(a, b)
    x = greatest_common_divisor_two_values(z, c)

    return x


print(greatest_common_divisor_three_values(a, b, c))


def greatestCommonDivisor(m, n):
    if n == 0:
        return m

    return greatestCommonDivisor(n, m % n)


print(greatestCommonDivisor(1304, 1024))


def extended_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


ea = 1432
eb = 123211


print(extended_gcd(ea,eb))
print('This gives -22973 and 267 for x and y, respectively')

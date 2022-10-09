'''
horner's method

 cnxn + cn-1xn-1 + cn-2xn-2 + … + c1x + c0
 f(x)=k=0∑n​ak​xk f(x) = sum[a(k) * x^(k)] where k = 0 and nth degree,
 i.e. deg(f(x)) = n where n represents the highest variable exponent. so if I had the values of a= [4,3,2] and x = 2

f(2) = [4 * 2^0] + [3 * 2^1] + [2 * 2^2]
f(2) = 18

1. Set k = n
2. Let bk = ak
3. Let bk - 1 = ak - 1 + bkx0
4. Let k = k - 1
5. If k ≥ 0 then go to step 3
Else End

another way to look at it

f(x)    = 2x^2 + 3x + 4
        = (x(2x + 3)) + 4


'''


def horner(a, x):
    n = len(a)
    p = a[0]

    for i in range(1, n):
        p = p * x + a[i]

    return p


a = [2, 3, 4]
x = 2
# 2x^2 + 3x + 4
# x= 2
# 8 + 6 + 4
print(horner(a, x))


def polynomial_long_division(a, x):
    result = [a[0]]
    for i in range(1, len(a)):
        result.append(a[i] + (x * result[i - 1]))
    return result, print(f'The remainder is {result[-1]}')


# f(x) = 2x**3 - 6x**2 + 2x - 1, x = 3
# x - 3 = 0
f = [2, -6, 2, -1]
print(polynomial_long_division(f, 3))

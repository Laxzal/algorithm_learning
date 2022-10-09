def nth_fermat_number(n):
    if n == 0:
        return 3
    else:
        val = 1
        for i in range(n):
            val *= nth_fermat_number(i)
    return val + 2


value = 10

print(nth_fermat_number(10))
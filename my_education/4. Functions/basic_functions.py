def taxes_calc(*args):
    return sum(args) * 0.13


print(taxes_calc(120, 150, 70))

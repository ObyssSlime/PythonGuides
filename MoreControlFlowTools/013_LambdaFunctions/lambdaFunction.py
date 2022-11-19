def make_increment(n):
    return lambda x: n + x

l = make_increment(22)

print(l(1))

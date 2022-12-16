i = 5
def f(arg = i):
    print(arg)

i = 6

#def g(a, L = []):
#    L.append(a)
#    return L

# if you don't want the default to be shared between subsequent calls
def g(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

f() # will print 5 because the default value is evaluated only once

# this make a difference when the default is a muttable object such a list, dictionary, or classes
print(g(1))
print(g(2))
print(g(3))

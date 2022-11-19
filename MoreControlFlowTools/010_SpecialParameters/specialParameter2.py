def foo(name, /, **kwds):
    return 'name' in kwds

result = foo(1, **{'name':1})
print(result)

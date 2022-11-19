def concat(*args, sep = '/'):
    return sep.join(args)

# NOrmally, these variadic arguments will be last in the list of formal parameters, Any formal parameters which occour after the *args parameter are keyword only
result = concat('earth', 'mars', 'venus', sep=',')
print(result)



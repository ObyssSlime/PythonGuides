def scope_test():
    
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam 
        spam = "global spam"

    spam = "test spam"
    
    do_local()
    print("after local assignment", spam) # return test spam
    do_nonlocal()
    print("after nonlocal assignment", spam) # return nonlocal spam
    do_global()
    print("after global assignment", spam) # return nonlocal spam

scope_test()
print("in global scope", spam) # return global spam

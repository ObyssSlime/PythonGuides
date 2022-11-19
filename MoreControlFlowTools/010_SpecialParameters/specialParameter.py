def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combine_arg(pos, /, standard, *, kwd):
    print(pos, standard, kwd)

standard_arg("ade") # passed by position or keyword
pos_only_arg(2)  # passed only position
kwd_only_arg(arg=3) # passed only keyword
combine_arg(1, 2, kwd=3) # passed position before '/', keyword after '*', and between both is standard argument

class MyClass:
    """ simple class """
    i = 12345 # nonlocal variable / class variable
    def __init__(self):
        self.data = [] # instance variable

    def f(self):
        return "Hello World"

x = MyClass() # instance
print(MyClass.i)
print(MyClass.f)
print(x.data)

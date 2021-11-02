def upper(func):
    def inner():
        str1 = func()
        return str1.upper()

    return inner


def another(func):
    def inner():
        str2 = func()
        return str2.split(" ")
    return inner

@another 
@upper
def string():
    return "something good"


#function decoraror woth parameter

def decorator(func):
    def inner(params):
        print(func)
        return func+params().upper()
    return inner

@decorator("sumit")
def mainFunC():
    return "i am"

#class decorator

def decorator(method):
    def check(params):
        print(params.name)
    return check

class test():
    def __init__(self,name):
        self.name = name
    
    @decorator
    def func(self):
        return self.name

ok = test("sumit")
ok.func()


#class test

class test():
    def __init__(self):
        self.counter = 1
    
    def inc(self):
        self.counter +=1

    def print(self):
        print(self.counter)

ok = test()
ok.inc()

ok.print()
ok.print()
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

def hifun(func):
    def inner(*args, **kwargs):
        print("-" * 30)
        func(*args, **kwargs)
        print("-" * 30)
    return inner

@percent
@star
@hifun
def printer(msg):
    print(msg)
printer("Hello")
#-------------------------------------------------
# Result :
# ******************************
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Hello
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ******************************
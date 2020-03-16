def partial_apply(func, arg):
    def inner(x):
        return func(arg, x)
    return inner


def flip(func):
    def inner(x, y):
        return func(y, x)
    return inner

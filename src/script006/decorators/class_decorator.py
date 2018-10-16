from functools import update_wrapper, wraps, lru_cache
class DecorClass(object):
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)
        pass

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs) * 2
        pass

class WrapperWithParams(object):
    def __init__(self, multiplier):
        self.multiplier = multiplier
        pass

    def __call__(self, func, *args, **kwargs):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * self.multiplier
        return wrapper




@DecorClass
def decorated1(i):return i

@WrapperWithParams(3)
def decorated3(i):return i


@WrapperWithParams(4)
def decorated4(i):return i



if __name__ == '__main__':
    fn1 = decorated1
    print(fn1(1))

    fn3 = decorated3
    print(fn3(1))

    fn4 = decorated4
    print(fn4(1))
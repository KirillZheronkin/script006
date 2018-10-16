


class A(object):

    def __new__(cls, *args, **kwargs):
        inst = super().__new__(*args, **kwargs)
        return inst


    def __init__(self, *args, **kwargs):
        pass



if __name__ == '__main__':
    a = A(1,2,3,key1="value1")
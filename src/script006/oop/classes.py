

class ClassA(object):

    my_args = None
    my_kwargs = None
    __my_property = None

    def __init__(self, *args,**kwargs):
        self.my_args = args
        self.my_kwargs = kwargs

    def my_method(self, *args, **kwargs):
        print(args, **kwargs)

    @property
    def my_property(self):
        return self.__my_property

    @my_property.setter
    def my_property(self, value):
        self.__my_property = value


if __name__ == '__main__':

    class_a = ClassA(1,2,3,4,5, x=2)
    print(class_a)
    print(class_a.__dict__)
    print(ClassA.__dict__)

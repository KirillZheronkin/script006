
def repr(this): return "object of {}".format(this.__class__)

class SimpleMetaClass(type):

    def __prepare__(name, inheritance):
        return {"свойство":"НОВОЕ"}

    def __new__(mcs,name,inheritance, props):
        props['proprety_added_by_metaclass'] = SimpleMetaClass.__name__
        new_class = super().__new__(mcs,name,inheritance, props)
        return new_class

    def __init__(cls, clsname, inheritance, props):
        super().__init__(clsname, inheritance, props)



class B(object, metaclass=SimpleMetaClass):

    prop1 ="prop1"
    def __repr__(self):
        return "instance of {} with id {}".format(self.__class__, id(self))




if __name__ == '__main__':
    b = B()
    c = SimpleMetaClass("C", (), {"__repr__": repr})()
    print("{}: {}".format(b, b.proprety_added_by_metaclass))
    print("{}: {}".format(c, c.proprety_added_by_metaclass))

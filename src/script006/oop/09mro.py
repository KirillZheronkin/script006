class MroMetaClass(type):

    def mro(cls):
        return (cls, D,C,B,A,object)

class A(object): pass
class B(object): pass

class D(A, B): pass
class C(B, A): pass


class E(
    D,
    C,
    metaclass=MroMetaClass
): pass








if __name__ == '__main__':
    e = E()
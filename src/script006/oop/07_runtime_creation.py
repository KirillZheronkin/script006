
class A(object): pass



if __name__ == '__main__':
    property_x = None
    method_y = lambda self: print("Im method y!")

    B = type("B", (A,), {'property_x': property_x, 'method_y': method_y})
    b = B()
    dir(b)




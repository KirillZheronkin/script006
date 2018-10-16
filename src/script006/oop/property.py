class WithXProperty(object):

    def __init__(self):
        self._x = None
    def get_x(self):
        print('getting x')
        return self._x
    def set_x(self, value):
        print('setting x')
        self._x = value
    def del_x(self):
        print("removing x property")
        self._x = 'removed'
    x = property(get_x, set_x, del_x, 'property X')



if __name__ == '__main__':
    ins = WithXProperty()
    print(ins.x)
    ins.x = 1
    del ins.x
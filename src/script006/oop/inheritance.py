class One(object):
    def method1(self):
        print(self.__class__)

    def method2(self):
        print(self.method2.__name__)

class Two(object):
    def method1(self):
        print("{} is the best".format(self.__class__))



class Three(Two, One):

    def method1(self):
        super().method1()
        print("called method1 from class Three!!!")



if __name__ == '__main__':
    three = Three()
    three.method1()
    three.method2()
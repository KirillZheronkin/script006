from .class_b import B
class C:
    def get_value(self):
        b = B()
        result = b.get_value(self)
        return result
import inspect

class AutoSlots(type):
# przykład wykorzystania metaklasy do automatycznego dodanie slots przed sworzeniem klasy
    def __new__(meta,name,bases,attrs):
        if "__init__" in attrs:
            slots = tuple(inspect.signature(attrs["__init__"]).parameters.keys())[1:]
            attrs["__slots__"] = slots
        return super().__new__(meta,name,bases,attrs)

class TestSlots(metaclass=AutoSlots):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

slots = TestSlots(1,2,3)
print(slots.b)
# print(slots.__dict__) AttributeError



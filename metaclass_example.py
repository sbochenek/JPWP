from datetime import date
class A:pass


class MetaExample(type):
    class_register = []
    objects_created = 0
    instance_register = {}

    def __new__(mcs, name, bases, attrs):
        # modyfikacja klas dziedziczacych dodanie klasy A do dziedziczenia
        if A not in bases:
            bases = tuple(list(bases) + [A])

        # modyfikacja atrybutow klasy
        attrs["data_created"] = date.today()
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        # rejestracja tworzonych klas
        if cls not in MetaExample.class_register:
            MetaExample.class_register.append(cls)
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        # fitrowanie argumentwo przy tworzeniu obiektu
        allowed_keys = {'x', 'y'}
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in allowed_keys}


        instance = super().__call__(*args, **filtered_kwargs)
        # Rejestracja obiektu
        MetaExample.instance_register[instance] = cls

        return instance


class Clas1(metaclass=MetaExample): pass
class Clas2(metaclass=MetaExample): pass
class Clas3(metaclass=MetaExample): pass

class Class(metaclass=MetaExample):
    def __init__(self, **kwargs):
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.z = kwargs.get('z')


obj = Class()
obj2 = Clas1()
obj3 = Clas2()
obj4 = Clas3()

obj1 = Class(x=1,y=2,z=100)
print(f"wymuszone dziedziczenie przez metaklase: {Class.__mro__}")
print(f"dodany atrybut przez metaklase: {Class.data_created}")
print(f"zarejestrowane klasy {MetaExample.class_register}")
print(f"wyfiltrowane argumenty {obj1.__dict__}")
print(f"zarejestrowane obiekty i ich klasy{MetaExample.instance_register}")
# https://github.com/JacobCallahan/Understanding/blob/master/Python/metaclasses/metaclasses.py

class NoisyMeta(type):
    @classmethod
    def __prepare__(meta, name, bases):
        print("Entering Meta __prepare__")
        print(f"{meta=}")
        print(f"Preparing: {name} with bases {bases}")
        namespace = super().__prepare__(name, bases)
        print(f"{namespace=}")
        print("Exiting Meta __prepare__")
        return namespace

    def __new__(meta, name, bases, attrs):
        print("Entering Meta __new__")
        print(f"{meta=}")
        print(f"Creating: {name} with bases {bases} and attrs {attrs}")
        result = super().__new__(meta, name, bases, attrs)
        print(f"{result=}")
        print("Exiting Meta __new__")
        return result

    def __init__(cls, name, bases, attrs):
        print("Entering Meta __init__")
        print(f"{cls=}")
        print(f"Initializing: {name} with bases {bases} and attrs {attrs}")
        result = super().__init__(name, bases, attrs)
        print(f"{result=}")
        print("Exiting Meta __init__")
        return result

    def __call__(cls, *args, **kwargs):
        print("Entering Meta __call__")
        print(f"{cls=}")
        print(f"Calling: {cls.__name__} with args {args} and kwargs {kwargs}")
        result = super().__call__(*args, **kwargs)
        print(f"{result=}")
        print("Exiting Meta __call__")
        return result


class Example(metaclass=NoisyMeta):
    print("<<<Beginning of Example class definition>>>")
    classvar = "test"
    print(f"<<<{classvar=}>>>")

    def __new__(cls, *args, **kwargs):
        print("<<<Entering class __new__>>>")
        print(f"<<<{cls=}, {args=}, {kwargs=}>>>")
        print("<<<Exiting class __new__>>>")
        return super().__new__(cls)

    def __init__(self, **kwargs):
        print("<<<Entering class __init__>>>")
        self.__dict__.update(kwargs)
        print(f"<<<{self.__dict__=}>>>")
        print("<<<Exiting class __init__>>>")

    print("<<<Middle of Example class definition>>>")

    def example_func(self):
        print(f"<<<{self.classvar=}>>>")

    print("<<<End of Example class definition>>>")


print("<<<Creating class object>>>")
exampl_instance = Example(a=1,b=2)
exampl_instance.example_func()


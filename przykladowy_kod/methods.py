class Methods:
    class_string = "test"
    class_list = []

    def __init__(self, inst_string):
        self.inst_string = inst_string
        self.inst_list = []

    def append_instance_list(self,arg):
        self.inst_list.append(arg)

    @classmethod
    def append_class_list(cls,arg):
        cls.class_list.append(arg)

    @staticmethod
    def int_to_str(arg):
        return str(arg)

    @classmethod
    def alternate_constructor(cls,arg):
        return cls(arg)

    # przyklad nadpisania metody specjalnej
    def __str__(self):
        return (f"nazwa klasy {self.__class__.__name__} jej string {self.inst_string}\n"
                f"jej bazowy string bez nadpisania {super().__str__()}")




instance_1 = Methods("instance 1")
instance_2 = Methods("instance 2")

# dodanie zmiennej klasowej metoda klasowa przez instanje i klase
Methods.append_class_list(1)
instance_2.append_class_list(2)
print(Methods.class_list)

# prosty przykład metody statycznej nie wymagajacej instanji klasy
print(type(Methods.int_to_str(6)))

# przykład uzycia metody klasowej do alternatywnego konstruktora
instance_3 = Methods.alternate_constructor('instance 3')
print(type(instance_3))

print(instance_1.__str__())

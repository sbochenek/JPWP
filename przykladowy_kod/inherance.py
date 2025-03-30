class A:pass
class B:pass
class C:pass
class D(A,B):pass
class E(C,):pass
class F(C,A):pass
class G(D,E,F):pass

class Base(G):
    def __init__(self,str_base):
        self.str_base = str_base

    def base_show(self):
        print(f"metoda w klasie bazowej i jego zmienna: {self.str_base}")

    def show(self):
        print("metoda w klasie bazowej")


class Base2:
    def __init__(self):
        print("konstruktor 2 klasy bazowej")


class SubClass(Base, Base2):
    def __init__(self,str_base,str_child):
        self.str_child = str_child
        super().__init__(str_base) # wymagane wywołanie konstruktora klasy bazowej
        # super odwołuje się tylko do pierwszej klasy w kolejność mro wykonanie kolejnych konstruktorów
        # wymaga ich jawnego wywołania
        Base2().__init__()

    def sub_show(self):
        print(f"metoda w podkalsie i jej zmienna: {self.str_child}")
        super().base_show() # wywolanie metody klasy nadrzednej

    # prosty przyklad nadpisanai metody
    def show(self):
        print("nadpisana metoda w podklasie")

child = SubClass("a","b")
child.sub_show()
child.show()

# pokazanie kolejności dziedziczenia klas
print(SubClass.__mro__)

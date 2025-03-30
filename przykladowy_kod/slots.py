import sys


class Slots:
    __slots__ = ('a1','a2','a3','a4')

    def __init__(self,a1,a2,a3,a4,):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4


class InheritanceSlots(Slots):
    def __init__(self,a1,a2,a3,a4,a5):
        super().__init__(a1,a2,a3,a4)
        self.a5 = a5


class NoSlots:
    def __init__(self,a1,a2,a3,a4):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

slots = Slots(1,2,3,4)
no_slots = NoSlots(1,2,3,4)
i_slots = InheritanceSlots(1,2,3,4,5)
i_slots.x = "nowa wartość w słowniku"  # dodanie nowego atrybutu w klasie nadrzednej niemożliwe

print("Rozmiar instancji slots:", sys.getsizeof(slots))
print("Rozmiar listy slots:", sys.getsizeof(slots.__slots__))
print("Rozmiar instancji no_slots:", sys.getsizeof(no_slots))
print("Rozmiar słownika dla no_slots:", sys.getsizeof(no_slots.__dict__))

# dziedziczenie tworzy słownik w klasie pochodnej o ile w klasie pochodnej nie znowu nie zdefiniujemy slots
# sprawdzenie zawartości słownika w klasie nadrzędnej wyrzuci błąd AttributeError
print("słownik i_slots:", i_slots.__dict__)
print("dziedziczone sloty:", i_slots.__slots__)

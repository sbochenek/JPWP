class z1:
    class_atr = "class"

    def __init__(self,atr):
        self.instance_atr = atr

    def set_class_atr(self, atr):
        self.class_atr = atr


a = z1(1)
b = z1(2)

print(a.class_atr)
print(b.class_atr)

a.set_class_atr("a")
print(a.class_atr)
print(b.class_atr)
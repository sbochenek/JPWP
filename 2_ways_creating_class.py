# I standardowy sposob tworzenia klasy nic ciekawego
class A:pass

class Standard(A):
    def __init__(self,arg1):
        self.arg1 = arg1

    def example_fun(self):
        print(f"przykładowa funkcja 1 i argument instancji {self.arg1}")


# II sposob tworzenia klasy
def example_fun(self):
    print(f"przykładowa funkcja 2 argument instancji {self.arg1}")

def init(self,arg1,):
    self.arg1 = arg1

namespace = {
    "__init__": init,
    "example_fun" : example_fun}
Example = type("Example",(A,),namespace)

example = Example(1)
standard = Standard(2)
standard.example_fun()
example.example_fun()
print(standard.arg1)
print(example.arg1)

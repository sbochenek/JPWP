class Private():

    def __init__(self, protected, private):
        self._protected = protected
        self.__private = private


    def geta2(self):
        return self.__private


z = Private(1,2)
print(z._protected)      # działa mimo łamania konwencji
# print(z.__a2)          # AttributeError
print(z.geta2())         # działa przez metode publiczna
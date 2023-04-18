class Pila():
    def __init__(self):
        self.pila = list()
    
    def __str__(self):
        salida = ""
        for elem in self.pila:
            salida += f"|{elem}"
        return salida + "<>"

    def Apilar(self, elemento):
        self.pila.append(elemento)
    def Desapilar(self):
        return self.pila.pop()

P = Pila();
P.Apilar(1)
P.Apilar(2)
P.Apilar((1,2,3))
print(P)
print( P.Desapilar())
P.Apilar(4)
print(P)

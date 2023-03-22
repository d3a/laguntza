class Cola():
    def __init__(self):
        self.cola = list()
    
    def __str__(self):
        salida = "<"
        for elem in self.cola:
            salida += f"{elem}|"
        return salida + "<"

    def Encolar(self, elemento):
        self.cola.append(elemento)
    def Desencolar(self):
        salida = None
        if len(self.cola) != 0:
            salida = self.cola[0]
            self.cola.pop(0)
        return salida

C = Cola();
C.Encolar(1)
C.Encolar(2)
C.Encolar((1,2,3))
print(C)
print( C.Desencolar())
C.Encolar(4)
C.Encolar(5)
print( C.Desencolar())
print(C)

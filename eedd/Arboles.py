class Nodo():
    def __init__(self, contenido, hijos = None):
        self.padre = ""
        self.contenido = contenido
        self.hijos = set()
        if hijos != None:
            if type(hijos) == Nodo:
                self.AsignarHijo(hijos)
            else:
                for elem in hijos:
                    self.AsignarHijo(elem)
    def __str__(self):
        return f'Nodo: {self.contenido}'
    def PrintArbol(self, tab = 0):
        tabu = " " * tab;
        print(f'{tabu}{self.contenido}')
        for i, elem in enumerate(self.hijos):
            elem.PrintArbol( tab+2 )

    def AsignarHijo(self, hijo):
        hijo.padre = self
        self.hijos.add(hijo)
    def BorrarHijo(self, hijo):
        self.hijos.discard(hijo)
    def TieneHijos(self):
        return len(self.hijos) != 0
    def OrdenarHijos(self):
        menor = {"contenido":"", "nodo":None }
        aux = list()
        aux_out = list()
        aux = self.hijos
        while len(aux) != 0:
            for elem in aux:
                if elem.contenido < menor['contenido']:
                    menor['contenido'] = elem.contenido
                    menor['nodo'] = elem.nodo
            aux_out.append(menor['nodo'])
            aux.remove(menor['nodo'])
        

class Arbol():
    def __init__(self, contenido, hijos = None):
        self.raiz = Nodo( contenido, hijos)
        self.puntero = self.raiz

    def AsignarHijo(self, hijo):
        if type(hijo) != Nodo:
            aux = Nodo(hijo)
        else:
            aux = hijo
        aux.padre = self.puntero
        self.puntero.AsignarHijo(aux)
        self.puntero = aux

    def SubirPuntero(self):
        self.puntero = self.puntero.padre

    def __str__(self):
        return f'Arbol: {self.raiz}'


a = Arbol( "Arbol", (Nodo("nodo1",None), Nodo("nodo2",None)) )
a.AsignarHijo( Nodo("Nodo1", Nodo("Nodo11")) )
a.SubirPuntero()
a.AsignarHijo( Nodo("Nodo2", Nodo("Nodo21")) )

a.raiz.PrintArbol()

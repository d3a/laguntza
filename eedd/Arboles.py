class Nodo():
    def __init__(self, contenido: str, hijos: tuple):
        self.padre = ""
        self.contenido = contenido
        self.hijos = set()
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


class Arbol():
    def __init__(self, contenido, hijos):
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

    def __str__(self):
        return f'Arbol: {self.raiz}'


a = Arbol( "Arbol", tuple(Nodo("nodo1"), Nodo("nodo2")) )
nodo3 = Nodo( "nodo3" )
nodo3.AsignarHijo( Nodo( "nodo31") )
a.raiz.AsignarHijo( nodo3 )
nodo3.AsignarHijo( Nodo( "nodo32") )
nodo3.AsignarHijo( Nodo( "nodo33") )
nodo3.AsignarHijo( Nodo( "nodo33") )
a.AsignarHijo( "nodo4" )
a.AsignarHijo( "nodo41" )
a.AsignarHijo( "nodo411" )
a.raiz.PrintArbol()

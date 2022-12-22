class Nodo():
    def __init__(self, contenido=None, hijos=None):
        self.padre = None
        self.contenido = contenido
        self.hijos = list()
        if hijos != None:
            if type(hijos) == Nodo:
                self.CrearHijo(hijos)
            else:
                for elem in hijos:
                    self.CrearHijo(elem)

    def __str__(self):
        return f'{self.contenido}'

    def PrintNodo(self):
        salida = f'Nodo:{self.contenido}|'
        for elem in self.hijos:
            salida += f'{elem}|'
        print(salida)
    
    def EsRaiz(self): return self.padre == self
    def TieneHijos(self): return len(self.hijos) != 0
    
    def AsignarPadre(self, padre): self.padre = padre
    def AsignarRaiz(self): self.padre = self
    def CrearHijo(self, hijo): hijo.AsignarPadre(self); self.hijos.append(hijo)
    def BorrarHijo(self, hijo): self.hijos.remove(hijo)
    def RecorrerNodo(self, funcion):
        # Aquí su código :D
        if self.TieneHijos():
            for elem in self.hijos:
                elem.RecorrerNodo(funcion)                    


class Arbol():
    # raiz = Nodo()
    # puntero = Nodo()

    def __init__(self, contenido=None, hijos=None, puntero=None, nodo=None):
        if nodo != None:
            self.raiz = nodo
            self.puntero = nodo
        else:
            self.raiz = Nodo(contenido,hijos)
            self.puntero = self.raiz if puntero == None else puntero
        self.raiz.PrintNodo()
        
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.iterador    = self.raiz()
        self.indice_hijo = 0
        return self.iterador
 
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
        if not self.TieneHijos():
            raise StopIteration
        
        self.hijos[self.indice_hijo]
        self.indice_hijo += 1
        self.iterador 
        self.puntero
        return self.iterador

    def EsRaiz(self): return self.raiz == self.puntero

    def CrearHijo(self, hijo):
        if type(hijo) != Nodo:
            aux = Nodo(hijo)
        else:
            aux = hijo
        aux.padre = self.puntero
        self.puntero = aux
    
    def MoverPuntero(self, nodo=None):
        if nodo == None or type(nodo) != Nodo:
            self.puntero = self.raiz
        elif nodo == 1:    
            self.puntero = self.puntero.padre
        else:    
            self.puntero = nodo

    def PrintArbol(self, tab=0, puntero=None):
        display_tab = " " * tab;
        print(f'{display_tab}{self.raiz.contenido}')
        for i, elem in enumerate(self.raiz.hijos):
            aux = Arbol( elem.contenido, elem.hijos, self.puntero )
            aux.PrintArbol( tab+2, puntero )


    def __str__(self):
        return f'Arbol: {self.raiz}'

def iterar_nodo(nodo):
    print(nodo)
    if not nodo.TieneHijos():
        yield None
    else:
        for elem in nodo.hijos:
            iterar_nodo(elem)
            yield elem



n21 = Nodo("Nodo521")
n2 = Nodo("Nodo52", n21)
n11 = Nodo("Nodo511")
n1 = Nodo("Nodo51", n11)
n = Nodo("Nodo5", (n1, n2))
a = Arbol("Arbol", n)

a.PrintArbol()

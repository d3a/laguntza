class Nodo():
    def __init__(self, padre=0, contenido=None, index=0, prof=0):
        self.index = index
        self.prof = prof
        self.padre = padre
        self.contenido = contenido
        self.hijos = list()
    
    def __str__(self):
        salida = f'N[{self.contenido}|{self.index}|{self.prof}]'
        salida += f'({self.padre}|'
        for elem in self.hijos:
            salida += f'|{elem}'
        salida += f')'
        return salida

    def print(self,data, tab=0,puntero=None):
        print(f'{display_tab}{self}{display_marca}')
        for i, elem in enumerate(self.hijos):
            data[elem].print( tab + 2, puntero )

        
class Arbol():
    def __init__(self, contenido=None):
        self.data = list()
        self.puntero = 0
        self.next = 0
        self.CrearNodo(contenido)

    def __str__(self):
        salida = f'A({self.puntero}|{self.next})'
        salida += str(self.Nodo())
        return salida

    def print_nodo(self,index=0,tab=0):
        display_tab = " " * tab;
        display_marca=""
        if index == self.puntero:
            display_marca=" <-"
        print(f'{display_tab}{self.data[index]}{display_marca}')
        for elem in self.data[index].hijos:
            self.print_nodo(elem,tab+2)
        
    def print(self):
        print(self)
        for elem in self.data[0].hijos:
            self.print_nodo(elem)

    def CrearNodo(self, contenido, puntero=None):
        if puntero != None:
            self.puntero = puntero
        if self.puntero == 0 and self.next == 0:
            prof = 0
        else:
            prof = self.data[self.puntero].prof + 1
        nodo_aux = Nodo(self.puntero, contenido, prof, self.next)
        self.data.append(nodo_aux)
        if self.next != 0:
            self.data[self.puntero].hijos.append(self.next)
        self.puntero = self.next
        self.next += 1
        return self.puntero

    def Nodo(self,indice=0):
        return self.data[indice]
    def NodoActual(self):
        return self.data[self.puntero]
    def NodoUltimo(self):
        return self.data[self.next-1]

def PrintNodo(arbol, indice):
    salida = f'Nodo:{arbol.data[indice].contenido}|'
    for elem in arbol.data[indice].hijos:
        salida += f'{elem}|'
    print(salida)

a = Arbol("aaa")
b=a.CrearNodo("B")
a.CrearNodo("B1")
a.CrearNodo("B11")
a.puntero=b
a.CrearNodo("B2")
a.CrearNodo("B21")
a.puntero=b
a.CrearNodo("B3")
a.CrearNodo("B31")
A = a.CrearNodo("A",0)
a.CrearNodo("A1")
a.CrearNodo("A2",A)

a.print()

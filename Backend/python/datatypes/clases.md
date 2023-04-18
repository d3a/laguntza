# Classes

## Estructura Báscia

```python
class NombreClase(Herencia1 [,...])
    #Propiedades Estáticas
    sprop1: [datatype] = [init_val]
    sprop2: [datatype] = [init_val]
    ....

    def __init__(self [,parametros...]):
        # Invocar al contructor
        super().__init__(...)
        # Si hay varias clases padre
        Herencia1.__init__(self, ...)
        Herencia2.__init__(self, ...)
        # Propiedades de objeto
        self.prop3 = [init_val]
        # Propiedades privadas
        self.__hprop4 = [init_val]
        # Propiedades magiacas
        #self.__class__.__name__
        #self.__dict__
        pass

    def __new__(self [,parametros...]):
        # No me ha quedado muy claro (?¿)
        pass

    def __del__(self):
        # Finalizador
        pass
    
    def __setitem__(self, key, val):
        # obj = NombreClase()
        # obj[clave] = valor
        self.array[key] = val

    def __getitem__(self, item):
        # obj = NombreClase()
        # valor = obj[clave]
        return self.array[item]

    def __delitem__(self, item):
        # obj = NombreClase()
        # valor = obj[clave]
        self.array[item].pop()

    def __dir__(self):
        # dir( obj )
        return [ lista de atributos ]

    def __repr__(self):
        # obj = NombreClase()
        # print(obj)
        return some_string
          
    def __add__(self, other):
        # obj = NombreClase()
        # print(obj + 'algun texto')
        return algo + other

    # Métodos Estáticos
    @staticmethod
    def smetodo([argumentos]):
        pass

    # Métodos de objeto
    def metodo1(self [,argumentos]):
        pass

    def metodo2(self [,argumentos]):
        pass
      
a = NombreClase.sprop1
NombreClase.smetodo(...)
obj = NombreClase(...)
a = obj.prop3
obj.metodo1(...)
```

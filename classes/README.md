# Classes

## Estructura Báscia
```python
class NombreClase(Herencia1 [,...])
    #Propiedades Estáticas
    sprop1: [datatype] = [init_val]
    sprop2: [datatype] = [init_val]
    ....

    def __init__(self):
        # Invocar al contructor
        super().__init__(...)
        # Si hay varias clases padre
        Herencia1.__init__(self, ...)
        Herencia2.__init__(self, ...)
        # Propiedades de objeto
        self.prop3 = [init_val]
        pass
    
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

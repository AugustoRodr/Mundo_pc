

class Orden:
    contadorOrden=0

    def __init__(self, computadoras:list):
        # la variable de computadoras es una lista de objetos
        Orden.contadorOrden+=1
        self.__id_orden=Orden.contadorOrden
        self.__computadoras= computadoras
        
    def __str__(self):
        computadora_str=''
        for computadora in self.__computadoras:
            computadora_str+=computadora.__str__()
        
        return f'Orden: {self.__id_orden}\n Computadoras: {computadora_str}'
        
    
    def agregar(self, computadora):
        # computadora debe ser de tipo object
        self.__computadoras.append(computadora)
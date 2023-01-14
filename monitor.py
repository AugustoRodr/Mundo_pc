
class Monitor:
    contadorMonitores=0
    def __init__(self, marca:str, tamanio:str):
        Monitor.contadorMonitores+=1
        self.__idMonitor=Monitor.contadorMonitores
        self.__marca=marca
        self.__tamanio=tamanio

    def __str__(self):
        return f'Monitor: Id: {self.__idMonitor}, Marca: {self.__marca}, Tamaño: {self.__tamanio}.'

    def get(self):
        return self.__idMonitor, self.__marca, self.__tamanio

    def set(self, marca, tamanio):
        self.__marca=marca
        self.__tamanio=tamanio


#monitor=Monitor('acer','21 pulgadas')
#print(monitor)
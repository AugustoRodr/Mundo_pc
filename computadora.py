from teclado import Teclado
from raton import Raton
from monitor import Monitor

class Computadora:
    contadorComputadoras=0
    def __init__(self, nombre:str, monitor, teclado, raton):
        # las variables monitor, teclado y raton deberan de ser de tipo object
        Computadora.contadorComputadoras+=1
        self.__idComputadora=Computadora.contadorComputadoras
        self.__nombre=nombre
        self.__teclado=teclado
        self.__raton=raton
        self.__monitor=monitor
    
    def __str__(self):
        return f'\n  {self.__nombre}: {self.__idComputadora}\n\t{self.__monitor}\n\t{self.__teclado}\n\t{self.__raton}'

#monitor1=Monitor('acer','21 pulgadas')
#teclado1=Teclado('hp','usb')
#raton1=Raton('genius','ps/2')
#computadora1= Computadora('hp',monitor1,teclado1,raton1)
#print(computadora1)
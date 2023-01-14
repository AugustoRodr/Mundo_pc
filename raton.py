from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones=0
    def __init__(self, marca, tipo_entrada):
        Raton.contadorRatones+=1
        self.__idRaton=Raton.contadorRatones
        self._marca=marca
        self._tipo_entrada=tipo_entrada
    
    def __str__(self):
        return f'Raton: Id: {self.__idRaton}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}.'




#raton=Raton('hp', 'usb')
#print(raton)
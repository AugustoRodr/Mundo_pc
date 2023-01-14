from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclado=0

    def __init__(self, marca, tipo_entrada):
        Teclado.contadorTeclado+=1
        self.__idTeclado=Teclado.contadorTeclado
        self._marca=marca
        self._tipo_entrada=tipo_entrada
    
    def __str__(self):
        return f'Teclado: Id: {self.__idTeclado}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}.'


#teclado=Teclado('hp', 'ps/2')
#print(teclado)
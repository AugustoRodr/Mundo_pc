
class DispositivoEntrada:

    def __init__(self, tipo_entrada, marca):
        #atributos protegidos
        self._marca=marca
        self._tipo_entrada=tipo_entrada
    
    def __str__(self):
        return f'Marca: {self._marca} Tipo de entrada: {self._tipo_entrada}'

    def get(self):
        return self._marca, self._tipo_entrada

    def set(self, marca, tipo_entrada):
        self._marca=marca
        self._tipo_entrada=tipo_entrada
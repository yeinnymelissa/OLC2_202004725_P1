from Analizador.Entorno import Tipo

class Simbolo():
    def __init__(self, nombre, valor, tipo_simbolo, tipo_dato, editable, linea, columna, num_ambiente):
        self.nombre = nombre
        self.valor = valor
        self.tipo_simbolo = tipo_simbolo
        self.tipo_dato = tipo_dato
        self.editable = editable
        self.num_ambiente = num_ambiente
        self.linea = linea
        self.columna = columna

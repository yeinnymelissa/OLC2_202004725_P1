class Error():
    def __init__(self, descripcion, tipo, linea, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        
class Error():
    def __init__(self, descripcion, tipo, ambiente, fechaHora, linea, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.ambiente = ambiente
        self.fechaHora = fechaHora
        self.linea = linea
        self.columna = columna

        
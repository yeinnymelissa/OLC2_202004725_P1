from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *

class Literal(Expresion):
    def __init__(self, valor, tipo, linea, columna):
        self.valor = valor
        self.tipo = tipo
        super().__init__(linea, columna)
    
    def run(self, env):
        if(self.tipo == TipoDato.i64):
            return {'valor': int(self.valor), 'tipo': TipoDato.i64}
        elif(self.tipo == TipoDato.f64):
            return {'valor': float(self.valor), 'tipo': TipoDato.f64}
        elif(self.tipo == TipoDato.char):
            return {'valor': self.valor, 'tipo': TipoDato.char}
        elif(self.tipo == TipoDato.string):
            return {'valor': self.valor, 'tipo': TipoDato.string}
        elif(self.tipo == TipoDato.bool):
            return {'valor': self.valor, 'tipo': TipoDato.bool}
        else:
            return {'valor': self.valor, 'tipo': TipoDato.error}

    def ast(self):
        pass
from Analizador.Entorno.Error import Error
from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import Singleton

class As(Expresion):
    def __init__(self, valor, tipo_convertir, linea, columna):
        self.valor = valor
        self.tipo_convertir = tipo_convertir
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        expre = self.valor.run(env)

        if(expre['tipo'] == TipoDato.i64):
            if(self.tipo_convertir == TipoDato.f64):
                return {'valor': float(expre['valor']), 'tipo': TipoDato.f64}
        elif(expre['tipo'] == TipoDato.f64):
            if(self.tipo_convertir == TipoDato.i64):
                return {'valor': int(expre['valor']), 'tipo': TipoDato.i64}
        else:
            error = Error("El valor no es valido para realizar una conversión.", "Semántico", self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)
            return
    
    def ast(self):
        pass
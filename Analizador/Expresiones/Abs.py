from Analizador.Entorno.Error import Error
from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import Singleton
from datetime import datetime

class Abs(Expresion):
    def __init__(self, valor, linea, columna):
        self.valor = valor
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        expre = self.valor.run(env)

        if(expre['tipo'] == TipoDato.i64):
            return {'valor': abs(expre['valor']), 'tipo': TipoDato.f64}
        elif(expre['tipo'] == TipoDato.f64):
            return {'valor': abs(expre['valor']), 'tipo': TipoDato.i64}
        else:
            now = datetime.now()
            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
            error = Error("El valor no es posible obtener el valor absoluto.", "Semántico", env.id,fechaHora, self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)
            return
    
    def ast(self):
        pass
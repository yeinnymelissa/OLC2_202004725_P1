from Analizador.Entorno.Error import Error
from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import Singleton
from datetime import datetime

class To_String(Expresion):
    def __init__(self, valor, linea, columna):
        self.valor = valor
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        expre = self.valor.run(env)
        print(expre['valor'])
        if(expre['tipo'] == TipoDato.str):
            return {'valor': expre['valor'], 'tipo': TipoDato.string}
        else:
            now = datetime.now()
            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
            error = Error("El valor no es posible convertir con to_string.", "Semántico", env.id,fechaHora, self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)
            return
    
    def ast(self):
        pass
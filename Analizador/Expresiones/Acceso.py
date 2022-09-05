from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import Singleton
from Analizador.Entorno.Error import *
from Analizador.Entorno.Tipo import *
from datetime import datetime

class Acceso(Expresion):
    def __init__(self, nombre, linea, columna):
        self.nombre = nombre
        super().__init__(linea, columna)
    
    def run(self, env):
        variable = env.getVariable(self.nombre)

        if(variable == None):
            singleton = Singleton.getInstance()
            now = datetime.now()
            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
            error = Error("Variable inexistente.", "Semántico", env.id, fechaHora, self.linea, self.columna)
            singleton.addError(error)
            return {'valor': None, 'tipo': TipoDato.error}
        
        if(variable.tipo_simbolo == TipoSimbolo.vector):
            return {'valor': variable.valor, 'tipo': TipoDato.vec}
        else:
            return {'valor': variable.valor, 'tipo': variable.tipo_dato}
    
    def ast(self):
        pass
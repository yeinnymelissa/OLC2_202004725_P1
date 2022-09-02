from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import Singleton
from Analizador.Entorno.Error import *
from Analizador.Entorno.Tipo import *

class Acceso(Expresion):
    def __init__(self, nombre, linea, columna):
        self.nombre = nombre
        super().__init__(linea, columna)
    
    def run(self, env):
        variable = env.getVariable(self.nombre)

        if(variable == None):
            singleton = Singleton.getInstance()
            error = Error("Variable inexistente.", "Semántico", self.linea, self.columna)
            singleton.addError(error)
            return {'valor': None, 'tipo': TipoDato.error}
        
        return {'valor': variable.valor, 'tipo': variable.tipo_dato}
    
    def ast(self):
        pass
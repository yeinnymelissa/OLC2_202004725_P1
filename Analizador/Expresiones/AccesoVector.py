from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import Singleton
from Analizador.Entorno.Error import *
from Analizador.Entorno.Tipo import *

class AccesoVector(Expresion):
    def __init__(self, nombre, expresion, linea, columna):
        self.nombre = nombre
        self.expresion = expresion
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        variable = env.getVariable(self.nombre)

        num = self.expresion.run(env)

        if(variable == None):
            error = Error("Variable inexistente.", "Semántico", self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)
            return {'valor': None, 'tipo': TipoDato.error}

        if(variable.tipo_simbolo == TipoSimbolo.vector):
            if(num['tipo'] == TipoDato.i64):
                if(num['valor'] < len(variable.valor)):
                    return {'valor': variable.valor[num['valor']], 'tipo': variable.tipo_dato}
                else:
                    error = Error("El valor a buscar dentro del vector es más grande que el tamaño del vector.", "Semántico", self.linea, self.columna)
                    singleton.addError(error)
                    print(error.descripcion)
                    return {'valor': None, 'tipo': TipoDato.error}
            else:
                error = Error("El valor a buscar dentro del vector debe ser numérico.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                return {'valor': None, 'tipo': TipoDato.error}
        else:
            error = Error("La variable con el nombre \""+str(self.nombre)+"\" no es un vector.", "Semántico", self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)
            return {'valor': None, 'tipo': TipoDato.error}


    def ast(self):
        pass
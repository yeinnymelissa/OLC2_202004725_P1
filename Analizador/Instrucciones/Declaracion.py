from Analizador.Instrucciones.Instruccion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import Singleton
from Analizador.Entorno.Error import *
from Analizador.Entorno.Tipo import *
from datetime import datetime


class Declaracion(Instruccion):
    def __init__(self, nombre, tipo, expresion, editable, linea, columna):
        self.nombre = nombre
        self.tipo = tipo
        self.expresion = expresion
        self.editable = editable
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()

        if(type(self.expresion).__name__ != "Vector"):
            expre = self.expresion.run(env)

            if(self.tipo != None):
                if(expre['tipo'] != self.tipo):
                    now = datetime.now()
                    fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                    error = Error("Declaración invalida, no se puede asignar un tipo "+ singleton.getTipo(expre['tipo'])+" a una variable tipo " + singleton.getTipo(self.tipo)+" .", "Semántico", env.id, fechaHora, self.linea, self.columna)
                    singleton.addError(error)
                    print(error.descripcion)
                    return
                
                envActual = env.guardar_variable(self.nombre, expre['valor'], self.tipo, self.editable, TipoSimbolo.variable, self.linea, self.columna)
                
                if envActual == False:
                    now = datetime.now()
                    fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                    error = Error("Declaración invalida, la variable con el nombre \""+str(self.nombre)+"\" ya existe.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                    singleton.addError(error)
                    print(error.descripcion)
                    return
                return
            else:
                if(expre['tipo'] != TipoDato.error):
                    envActual = env.guardar_variable(self.nombre, expre['valor'], expre['tipo'], self.editable, TipoSimbolo.variable, self.linea, self.columna)
                    
                    if envActual == False:
                        now = datetime.now()
                        fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                        error = Error("Declaración invalida, la variable con el nombre \""+str(self.nombre)+"\" ya existe.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                        singleton.addError(error)
                        print(error.descripcion)
                        return
                    return
        else:
            expre = self.expresion.run(env)
            if(expre['tipo'] != TipoDato.error):
                envActual = env.guardar_variable(self.nombre, expre['valor'], expre['tipo'], self.editable, TipoSimbolo.vector, self.linea, self.columna)
                
                if envActual == False:
                    now = datetime.now()
                    fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                    error = Error("Declaración invalida, la variable con el nombre \""+str(self.nombre)+"\" ya existe.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                    singleton.addError(error)
                    print(error.descripcion)
                    return
                return


    def ast():
        pass

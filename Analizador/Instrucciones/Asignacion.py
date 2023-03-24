from Analizador.Instrucciones.Instruccion import *
from Analizador.Singleton.Singleton import *
from Analizador.Entorno.Entorno import *
from datetime import datetime

class Asignacion(Instruccion):
    def __init__(self, nombre,expresion, linea, columna):
        self.nombre = nombre
        self.expresion = expresion
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        expresion = self.expresion.run(env)
        bandera = True

        variable = env.getVariable(self.nombre)

        if(variable == None):
            error = Error("La variable con el nombre \""+self.nombre+"\" no existe.", "Semántico", self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)
            bandera = False
        
        if(variable != None):
            if(variable.editable == False):
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("La variable con el nombre \""+self.nombre+"\" no se puede modificar porque es constante.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                bandera = False
            if(variable.tipo_dato != expresion['tipo']):
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("La asignacion no se puede realizar porque la variable es tipo "+singleton.getTipo(variable.tipo_dato)+" y se le quiere asignar un tipo "+singleton.getTipo(expresion['tipo'])+".", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                bandera = False
        
        if(bandera == True):
            env.actualizarVariable(self.nombre, expresion['valor'])
    
    def ast(self):
        pass
        


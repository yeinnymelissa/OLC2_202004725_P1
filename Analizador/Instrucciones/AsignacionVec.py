from Analizador.Instrucciones.Instruccion import *
from Analizador.Singleton.Singleton import *
from Analizador.Entorno.Entorno import *
from datetime import datetime

class AsignacionVec(Instruccion):
    def __init__(self, nombre, num, expresion, linea, columna):
        self.nombre = nombre
        self.num = num
        self.expresion = expresion
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        expresion = self.expresion.run(env)
        bandera = True

        variable = env.getVariable(self.nombre)

        if(variable == None):
            now = datetime.now()
            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
            error = Error("La variable con el nombre \""+self.nombre+"\" no existe.", "Semántico", env.id, fechaHora, self.linea, self.columna)
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
                if(variable.tipo_dato == TipoDato.str and expresion['tipo'] == TipoDato.string):
                    nume = self.num.run(env)
                    if nume['tipo'] == TipoDato.i64:
                        variable.valor[nume['valor']] = expresion['valor']
                    else:
                        now = datetime.now()
                        fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                        error = Error("El valor a buscar dentro del vector debe ser numérico.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                        singleton.addError(error)
                        print(error.descripcion)
                    return
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("La asignacion no se puede realizar porque la variable es tipo "+singleton.getTipo(variable.tipo_dato)+" y se le quiere asignar un tipo "+singleton.getTipo(expresion['tipo'])+".", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                bandera = False
        
        if(bandera == True):
            nume = self.num.run(env)

            if nume['tipo'] == TipoDato.i64:
                if(nume['valor'] < len(variable.valor)):
                    variable.valor[nume['valor']] = expresion['valor']
                else:
                    now = datetime.now()
                    fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                    error = Error("El valor a buscar dentro del vector es más grande que el tamaño del vector.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                    singleton.addError(error)
                    print(error.descripcion)
                    return
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("El valor a buscar dentro del vector debe ser numérico.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
    
    def ast(self):
        pass
        
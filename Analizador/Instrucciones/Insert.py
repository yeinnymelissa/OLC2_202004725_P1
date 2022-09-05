from Analizador.Entorno.Entorno import Entorno
from Analizador.Entorno.Error import Error
from Analizador.Entorno.Tipo import *
from Analizador.Instrucciones.Instruccion import Instruccion
from Analizador.Singleton.Singleton import Singleton
from datetime import datetime

class Insert(Instruccion):
    def __init__(self, nombre, posicion, expresion, linea, columna):
        self.nombre = nombre
        self.posicion = posicion
        self.expresion = expresion
        super().__init__(linea, columna)

    def run(self, env):
        singleton = Singleton.getInstance()

        vector = env.getVariable(self.nombre)

        pos = self.posicion.run(env)

        expre = self.expresion.run(env)

        if vector != None:
            if vector.tipo_simbolo == TipoSimbolo.vector:
                if vector.editable == True:
                    if(expre['tipo'] == vector.tipo_dato):
                        if(pos['tipo'] == TipoDato.i64):
                            if(pos['valor'] < len(vector.valor)):
                                vector.valor.insert(pos['valor'], expre['valor'])
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
                            return
                    else:
                        now = datetime.now()
                        fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                        error = Error("El tipo de dato que se le quiere asignar al vector no es compatible con el tipo de dato del vector.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                        singleton.addError(error)
                        print(error.descripcion)
                        return
                else:
                    now = datetime.now()
                    fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                    error = Error("El vector con el nombre \""+str(self.nombre)+"\" no es editable.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                    singleton.addError(error)
                    print(error.descripcion)
                    return
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("La variable con el nombre \""+str(self.nombre)+"\" no es un vector para realizar una instruccion insert().", "Semántico", env.id, fechaHora,  self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                return
        else:
            now = datetime.now()
            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
            error = Error("El con el nombre \""+str(self.nombre)+"\" no existe.", "Semántico", env.id, fechaHora, self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)
            return

    def ast(self):
        pass
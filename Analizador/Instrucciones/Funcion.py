from Analizador.Instrucciones.Instruccion import *
from Analizador.Singleton.Singleton import *
from Analizador.Entorno.Entorno import *
from datetime import datetime

class Funcion(Instruccion):

    ambienteFuncion = None

    def __init__(self, nombre, bloque, parametros, tipo, linea, columna):
        self.nombre = nombre
        self.bloque = bloque
        self.parametros = parametros
        self.tipo = tipo
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        funcionEncontrada = env.buscar_variable(self.nombre)

        self.ambienteFuncion = Entorno(singleton.getContador(), env)

        singleton.aumentarEnv()

        if funcionEncontrada == True:
            now = datetime.now()
            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
            error = Error("Ya existe un dato con el nombre \""+self.nombre+"\".", "Semántico", env.id, fechaHora, self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)
            return
        
        for param in self.parametros:
            param.run(self.ambienteFuncion)
        
        env.guardar_variable(self.nombre, self, self.tipo, False, TipoSimbolo.funcion, self.linea, self.columna)
    
    def ast(self):
        pass
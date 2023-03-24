from Analizador.Instrucciones.Instruccion import *
from Analizador.Singleton.Singleton import *
from Analizador.Entorno.Entorno import *
from datetime import datetime

class Main(Instruccion):

    def __init__(self,bloque, linea, columna):
        self.nombre = "main"
        self.bloque = bloque
        super().__init__(linea, columna)
    
    def run(self, env):
        print("ADENTRO MAIN")
        singleton = Singleton.getInstance()

        funcionEncontrada = env.buscar_variable(self.nombre)

        if funcionEncontrada == True:
            now = datetime.now()
            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
            error = Error("Ya existe un dato con el nombre \""+self.nombre+"\".", "Semántico", env.id, fechaHora, self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)
            return
        
        env.guardar_variable(self.nombre, self, None, False, TipoSimbolo.funcion, self.linea, self.columna)

        if self.bloque != None:
            self.bloque.run(env)
    
    def ast(self):
        pass
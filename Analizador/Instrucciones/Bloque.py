from Analizador.Instrucciones.Instruccion import *
from Analizador.Singleton.Singleton import *
from Analizador.Entorno.Entorno import *
from datetime import datetime

class Bloque(Instruccion):
    def __init__(self, instrucciones, linea, columna):
        self.instrucciones = instrucciones
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        
        newEnv = Entorno(singleton.getContador(), env)

        singleton.aumentarEnv()

        #print("NEW: "+ str(newEnv.id))

        for ins in self.instrucciones:
            ins.run(newEnv)
    
    def ast(self):
        pass




        
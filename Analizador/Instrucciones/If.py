from Analizador.Instrucciones.Instruccion import *
from Analizador.Singleton.Singleton import *
from Analizador.Entorno.Entorno import *
from datetime import datetime

class If(Instruccion):
    def __init__(self, condicion, bloque, elseif, linea, columna):
        self.condicion = condicion
        self.bloque = bloque
        self.elseif = elseif
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        condicion = self.condicion.run(env)
        
        if condicion['tipo'] == TipoDato.bool:
            if(condicion == True):
                self.bloque.run(env)
                return True
            elif self.elseif != None:
                bandera = False
                for el in self.elseif:
                    if(bandera == False):
                        bandera = el.run(env)
            else:
                return False
    def ast(self):
        pass

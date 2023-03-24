from Analizador.Instrucciones.Instruccion import *
from Analizador.Singleton.Singleton import *
from Analizador.Entorno.Entorno import *
from datetime import datetime

class If(Instruccion):
    def __init__(self, condicion, bloque, elseif, elsi, linea, columna):
        self.condicion = condicion
        self.bloque = bloque
        self.elseif = elseif
        self.elsi = elsi
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        condicion = self.condicion.run(env)
        bandera = False

        if condicion['tipo'] == TipoDato.bool:
            if(condicion['valor'] == True):
                self.bloque.run(env)
                return True
            elif self.elseif != None:
                for el in self.elseif:
                    if(bandera == False):
                        if(el != None):
                            bandera = el.run(env)
                if self.elsi != None and bandera == False:
                    self.elsi.run(env)
            elif self.elsi != None and bandera == False:
                self.elsi.run(env)
            else:
                return False
    def ast(self):
        pass

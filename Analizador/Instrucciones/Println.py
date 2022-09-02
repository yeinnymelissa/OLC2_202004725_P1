from Analizador.Entorno.Entorno import Entorno
from Analizador.Entorno.Error import Error
from Analizador.Entorno.Tipo import *
from Analizador.Instrucciones.Instruccion import Instruccion
from Analizador.Singleton.Singleton import Singleton

class Println(Instruccion):
    def __init__(self, formato, expresion, linea, columna):
        self.formato = formato
        self.expresion = expresion
        super().__init__(linea, columna)

    def run(self, env):
        singleton = Singleton.getInstance()

        if self.formato == None:
            expre = self.expresion.run(env)
            if expre['tipo'] == TipoDato.string:
                singleton.addConsola(expre['valor'] + "\n")
            else:
                error = Error("Para imprimir sin formato se debe imprimir un dato tipo String.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
            return
        else:
            formato = self.formato.split(' ')
            express = 0
            vec = 0
            cadena = ""

            for i in formato:
                if i == "{}":
                    express += 1
                elif i == "{:?}":
                    vec += 1
            if express > 0:
                if express == len(self.expresion):
                    for i in formato:
                        if i != "{}" and i != "{:?}":
                            cadena += i +" "
                    singleton.addConsola(cadena)
                    for i in self.expresion:
                        ex = i.run(env)
                        singleton.addConsola(str(ex['valor'])+" ")
                    pass
                    singleton.addConsola("\n")
                

            
    
    def ast(self):
        pass
        
    
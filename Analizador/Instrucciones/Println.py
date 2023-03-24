from re import A
from Analizador.Entorno.Entorno import Entorno
from Analizador.Entorno.Error import Error
from Analizador.Entorno.Tipo import *
from Analizador.Instrucciones.Instruccion import Instruccion
from Analizador.Singleton.Singleton import Singleton
from datetime import datetime

class Println(Instruccion):
    def __init__(self, formato, expresion, linea, columna):
        self.formato = formato
        self.expresion = expresion
        super().__init__(linea, columna)

    def run(self, env):
        singleton = Singleton.getInstance()

        if self.formato == None:
            expre = self.expresion.run(env)
            print("Tipo: "+ str(expre['tipo']))
            if expre['tipo'] == TipoDato.str:
                singleton.addConsola(expre['valor'] + "\n")
            elif expre['tipo'] == TipoDato.string:
                singleton.addConsola(expre['valor'] + "\n")
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("Para imprimir sin formato se debe imprimir un dato tipo String.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
            return
        else:
            formato = self.formato.split(' ')
            express = 0
            vec = 0
            cadena = ""
            for i in range(0, len(formato)) :
                if formato[i] == "{}":
                    express += 1
                    formato[i] = "espacio"
                elif formato[i] == "{:?}":
                    vec += 1
                    formato[i] = "espacio"
            if express > 0:
                if express == len(self.expresion):
                    contador = 0
                    valores = []
                    for i in self.expresion:
                        ex = i.run(env)
                        if ex['tipo'] != TipoDato.vec:
                            print("PASE VALORES")
                            print(str(ex['valor']))
                            valores.append(str(ex['valor']))
                            #singleton.addConsola(str(ex['valor'])+" ")
                        else: 
                            now = datetime.now()
                            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                            error = Error("No se puede imprimir con el formato {} un vector.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                            singleton.addError(error)
                            print(error.descripcion)
                    for i in formato:
                        if i == "espacio":
                            i = valores[contador]
                            contador += 1
                        cadena += i + " "
                    singleton.addConsola(cadena)
                    singleton.addConsola("\n")
            
            elif vec > 0:
                if vec == len(self.expresion):
                    contador = 0
                    valores = []
                    for i in self.expresion:
                        ex = i.run(env)
                        if ex['tipo'] == TipoDato.vec:
                            valores.append(str(ex['valor']))
                            #singleton.addConsola(str(ex['valor']))
                        else: 
                            now = datetime.now()
                            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                            error = Error("No se puede imprimir con el formato {:?} un valor que no sea vector.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                            singleton.addError(error)
                            print(error.descripcion)
                            return
                    for i in formato:
                        if i == "espacio":
                            i = valores[contador]
                            contador += 1
                        cadena += i + " "
                    singleton.addConsola(cadena)
                    singleton.addConsola("\n")
            
        
    
    def ast(self):
        pass
        
    
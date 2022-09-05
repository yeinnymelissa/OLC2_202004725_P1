from Analizador.Entorno import Tipo
from Analizador.Entorno.Error import Error
from Analizador.Entorno.Simbolo import Simbolo
from Analizador.Entorno.Tipo import *

class Singleton():
    instance = None
    def __init__(self):
        self.consola = ""
        self.ast = ""
        self.errores = []
        self.simbolos = []
        self.contadorEnv = 1

    @staticmethod
    def getInstance():
        if Singleton.instance == None:
            Singleton.instance = Singleton()
        return Singleton.instance

    def borrarTodo(self):
        self.consola = ""
        self.ast = ""
        self.errores = []
        self.simbolos = []
        self.contadorEnv = 1

    def addConsola(self, entrada):
        self.consola += entrada
    
    def getConsola(self):
        return self.consola

    def addError(self, error):
        self.errores.append(error)
    
    def getError(self):
        err = []
        cont = 1
        for error in self.errores:
            aux = [cont, error.descripcion, "Ambiente "+str(error.ambiente), error.linea, error.columna, error.fechaHora, error.tipo]
            err.append(aux)
            cont +=1
        return err
    
    def addSimbolo(self, simbolo):
        self.simbolos.append(simbolo)
    
    def getSimbolo(self):
        simbol = []
        for simbolo in self.simbolos:
            aux = [simbolo.nombre, self.getTipoSimbolo(simbolo.tipo_simbolo), self.getTipo(simbolo.tipo_dato), "Ambiente "+str(simbolo.num_ambiente), simbolo.linea, simbolo.columna]
            simbol.append(aux)
        return simbol

    def getContador(self):
        return self.contadorEnv

    def aumentarEnv(self):
        self.contadorEnv += 1
    
    def getTipo(self, tipo):
        if(tipo == TipoDato.i64):
            return "i64"
        elif(tipo == TipoDato.f64):
            return "f64"
        elif(tipo == TipoDato.bool):
            return "bool"
        elif(tipo == TipoDato.string):
            return "string"
        elif(tipo == TipoDato.char):
            return "char"
        else:
            return "error"
        
    def getTipoSimbolo(self, tipo):
        
        if(tipo == TipoSimbolo.funcion):
            return "Funcion"
        elif(tipo == TipoSimbolo.variable):
            return "Variable"
        elif(tipo == TipoSimbolo.vector):
            return "Vector"

    

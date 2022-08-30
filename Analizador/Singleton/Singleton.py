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

    def addConsola(self, entrada):
        self.consola += entrada
    
    def getConsola(self):
        return self.consola

    def addError(self, error):
        self.errores.append(error)
    
    def getError(self):
        return self.errores
    
    def addSimbolo(self, simbolo):
        self.simbolos.append(simbolo)

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

    

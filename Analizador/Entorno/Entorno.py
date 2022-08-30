from operator import truediv
from Analizador.Singleton.Singleton import Singleton
from Simbolo import *

class Entorno():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tabla_simbolos = {}
        self.entorno_anterior = None
        self.id = None

    def guardar_variable(self, nombre, valor, tipo_dato, editable, tipo_simbolo, linea, columna):
        
        if self.buscar_variable(nombre) == False :
            simbolo = Simbolo(nombre, valor, tipo_simbolo, tipo_dato, editable, linea, columna, self.id)
            self.tabla_simbolos[nombre] = simbolo
            singleton = Singleton.getInstance()
            singleton.addSimbolo(simbolo)
            return True
        return False

    def buscar_variable(self, nombre):
        if(self.tabla_simbolos.get(nombre) != None):
            return True
        else:
            return False
            

    def asignarAnterior(self, anterior):
        self.entorno_anterior = anterior
    
    def getVariable(self, nombre):
        env = self
        while env != None:
            if(self.tabla_simbolos.get(nombre) != None):
                return self.tabla_simbolos.get(nombre)
            env = env.entorno_anterior
        return None

    def obtenerValor(self, nombre):
        simbolo = self.tabla_simbolos.get(nombre, None)
        if simbolo != None:
            return simbolo
        tmp_anterior = self.entorno_anterior
        while tmp_anterior != None:
            simbolo = tmp_anterior.tabla_simbolos.get(nombre, None)
            if simbolo != None:
                return simbolo
            tmp_anterior = tmp_anterior.entorno_anterior
        return None

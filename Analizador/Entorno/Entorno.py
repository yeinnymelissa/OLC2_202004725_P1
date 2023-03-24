from operator import truediv
from Analizador.Entorno.Simbolo import Simbolo
from Analizador.Singleton.Singleton import Singleton

class Entorno():
    def __init__(self, id, entorno_anterior):
        self.tabla_simbolos = {}
        self.entorno_anterior = entorno_anterior
        self.id = id

    def guardar_variable(self, nombre, valor, tipo_dato, editable, tipo_simbolo, linea, columna):
        
        if self.buscar_variable(nombre) == False :
            simbolo = Simbolo(nombre, valor, tipo_simbolo, tipo_dato, editable, linea, columna, self.id)
            self.tabla_simbolos[nombre] = simbolo
            singleton = Singleton.getInstance()
            singleton.addSimbolo(simbolo)
            self.recorrerTablaSimbolos()
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
            if(env.tabla_simbolos.get(nombre) != None):
                return env.tabla_simbolos.get(nombre)
            env = env.entorno_anterior
        return None

    def actualizarVariable(self, nombre, valor):
        env = self

        while env != None:
            if(env.tabla_simbolos.get(nombre) != None):
                variable = env.tabla_simbolos.get(nombre)
                variable.valor = valor
                self.recorrerTablaSimbolos()
                return 
            env = env.entorno_anterior
    
    def recorrerTablaSimbolos(self):
        for simbolo in self.tabla_simbolos:
            valor = self.tabla_simbolos[simbolo]
            print(str(simbolo) +": "+str(valor.nombre) +" / " + str(valor.valor))

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

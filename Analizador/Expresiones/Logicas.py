from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import *
from datetime import datetime

class Logicas(Expresion):
    def __init__(self, izq, der, tipo, linea, columna):
        self.izq = izq
        self.der = der
        self.tipo = tipo
        super().__init__(linea, columna)
    
    def run(self, env):
        nodoIzq = self.izq.run(env)
        if(self.der != None):
            nodoDer = self.der.run(env)
        singleton = Singleton.getInstance()
        resultado = {'valor': None, 'tipo': TipoDato.error}

        if(self.tipo == TipoLogicas.AND):
            if nodoIzq['tipo'] == TipoDato.bool and nodoDer['tipo'] == TipoDato.bool:
                if(nodoIzq['valor'] == True and nodoDer['valor'] == True):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                elif(nodoIzq['valor'] == True and nodoDer['valor'] == False): 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
                elif(nodoIzq['valor'] == False and nodoDer['valor'] == True): 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
                elif(nodoIzq['valor'] == False and nodoDer['valor'] == False): 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("Los datos a comparar deben ser de tipo bool.", "Semántico",env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoLogicas.OR):
            if nodoIzq['tipo'] == TipoDato.bool and nodoDer['tipo'] == TipoDato.bool:
                if(nodoIzq['valor'] == True and nodoDer['valor'] == True):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                elif(nodoIzq['valor'] == True and nodoDer['valor'] == False): 
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                elif(nodoIzq['valor'] == False and nodoDer['valor'] == True): 
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                elif(nodoIzq['valor'] == False and nodoDer['valor'] == False): 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("Los datos a comparar deben ser de tipo bool.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoLogicas.NOT):
            if nodoIzq['tipo'] == TipoDato.bool:
                if(nodoIzq['valor'] == True):
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
                elif(nodoIzq['valor'] == False): 
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("Los datos a comparar deben ser de tipo bool.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        
        return resultado
    
    def ast(self):
        pass
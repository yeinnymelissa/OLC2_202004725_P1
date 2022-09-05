from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import *
from datetime import datetime

class Aritmeticas(Expresion):
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

        if(self.tipo == TipoAritmetica.suma):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                resultado = {'valor': nodoIzq['valor'] + nodoDer['valor'], 'tipo': TipoDato.i64}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                resultado = {'valor': nodoIzq['valor'] + nodoDer['valor'], 'tipo': TipoDato.f64}
            elif nodoIzq['tipo'] == TipoDato.str and nodoDer['tipo'] == TipoDato.str:
                resultado = {'valor': str(nodoIzq['valor']) + str(nodoDer['valor']), 'tipo': TipoDato.str}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("No se puede realizar la suma porque los tipos no son válidos.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoAritmetica.resta):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                resultado = {'valor': nodoIzq['valor'] - nodoDer['valor'], 'tipo': TipoDato.i64}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                resultado = {'valor': nodoIzq['valor'] - nodoDer['valor'], 'tipo': TipoDato.f64}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("No se puede realizar la resta porque los tipos no son válidos.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoAritmetica.multiplicacion):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                resultado = {'valor': nodoIzq['valor'] * nodoDer['valor'], 'tipo': TipoDato.i64}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                resultado = {'valor': nodoIzq['valor'] * nodoDer['valor'], 'tipo': TipoDato.f64}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("No se puede realizar la multiplicación porque los tipos no son válidos.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoAritmetica.division):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                print(nodoIzq['valor'] / nodoDer['valor'])
                if(type(nodoIzq['valor'] / nodoDer['valor']) == int):
                    resultado = {'valor': nodoIzq['valor'] / nodoDer['valor'], 'tipo': TipoDato.i64}
                elif(type(nodoIzq['valor'] / nodoDer['valor']) == float):
                    resultado = {'valor': nodoIzq['valor'] / nodoDer['valor'], 'tipo': TipoDato.f64}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                resultado = {'valor': nodoIzq['valor'] / nodoDer['valor'], 'tipo': TipoDato.f64}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("No se puede realizar la división porque los tipos no son válidos.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoAritmetica.powi):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                resultado = {'valor': nodoIzq['valor'] ** nodoDer['valor'], 'tipo': TipoDato.i64}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("No se puede realizar la potencia porque los tipos no son válidos.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoAritmetica.powf):
            if nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                resultado = {'valor': nodoIzq['valor'] ** nodoDer['valor'], 'tipo': TipoDato.f64}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("No se puede realizar la potencia porque los tipos no son válidos.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoAritmetica.modulo):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                resultado = {'valor': nodoIzq['valor'] % nodoDer['valor'], 'tipo': TipoDato.i64}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                resultado = {'valor': nodoIzq['valor'] % nodoDer['valor'], 'tipo': TipoDato.f64}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("No se puede realizar la multiplicación porque los tipos no son válidos.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoAritmetica.negado):
            if nodoIzq['tipo'] == TipoDato.i64:
                resultado = {'valor': nodoIzq['valor'] * (-1), 'tipo': TipoDato.i64}
            elif nodoIzq['tipo'] == TipoDato.f64:
                resultado = {'valor': nodoIzq['valor'] * (-1), 'tipo': TipoDato.f64}
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("No se puede realizar el negado porque los tipos no son válidos.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        else:
            now = datetime.now()
            fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
            error = Error("Opción aritmetica no válida.", "Semántico", env.id, fechaHora, self.linea, self.columna)
            singleton.addError(error)
            print(error.descripcion)

        return resultado
    
    def ast(self):
        pass
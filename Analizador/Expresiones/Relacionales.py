from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import *

class Relacionales(Expresion):
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

        if(self.tipo == TipoRelacionales.mayor):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                if(nodoIzq['valor'] > nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                if(nodoIzq['valor'] > nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.string and nodoDer['tipo'] == TipoDato.string:
                if(nodoIzq['valor'] > nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            else:
                error = Error("No se pudo realizar la operación relacional.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoRelacionales.menor):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                if(nodoIzq['valor'] < nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                if(nodoIzq['valor'] < nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.string and nodoDer['tipo'] == TipoDato.string:
                if(nodoIzq['valor'] < nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            else:
                error = Error("No se pudo realizar la operación relacional.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoRelacionales.mayorIgual):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                if(nodoIzq['valor'] >= nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                if(nodoIzq['valor'] >= nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.string and nodoDer['tipo'] == TipoDato.string:
                if(nodoIzq['valor'] >= nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            else:
                error = Error("No se pudo realizar la operación relacional.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoRelacionales.menorIgual):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                if(nodoIzq['valor'] <= nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                if(nodoIzq['valor'] <= nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.string and nodoDer['tipo'] == TipoDato.string:
                if(nodoIzq['valor'] <= nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            else:
                error = Error("No se pudo realizar la operación relacional.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoRelacionales.igualacion):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                if(nodoIzq['valor'] == nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                if(nodoIzq['valor'] == nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.string and nodoDer['tipo'] == TipoDato.string:
                if(nodoIzq['valor'] == nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            else:
                error = Error("No se pudo realizar la operación relacional.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
        elif(self.tipo == TipoRelacionales.diferente):
            if nodoIzq['tipo'] == TipoDato.i64 and nodoDer['tipo'] == TipoDato.i64:
                if(nodoIzq['valor'] != nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.f64 and nodoDer['tipo'] == TipoDato.f64:
                if(nodoIzq['valor'] != nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            elif nodoIzq['tipo'] == TipoDato.string and nodoDer['tipo'] == TipoDato.string:
                if(nodoIzq['valor'] != nodoDer['valor']):
                    resultado = {'valor': True, 'tipo': TipoDato.bool}
                else: 
                    resultado = {'valor': False, 'tipo': TipoDato.bool}
            else:
                error = Error("No se pudo realizar la operación relacional.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)

        return resultado

    def ast(self):
        pass
from Analizador.Expresiones.Expresion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import Singleton
from Analizador.Entorno.Error import *
from Analizador.Entorno.Tipo import *

class Vector(Expresion):
    def __init__(self, expresion, tipo_vector, linea, columna):
        self.expresion = expresion
        self.tipo_vector = tipo_vector
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()
        if (self.tipo_vector == TipoVectores.valoresIniciales):
            vec = []
            tipo = []
            bandera = False
            for expre in self.expresion:
                ex = expre.run(env)
                vec.append(ex['valor'])
                tipo.append(ex['tipo'])
            
            for tip in tipo: 
                if(tip != tipo[0]):
                    bandera = True
            
            if bandera == True:
                error = Error("Los tipos del vector son diferentes.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                return
            elif bandera == False:
                return {'valor': vec, 'tipo': tipo[0]}

        elif (self.tipo_vector == TipoVectores.repetidos):
             
            val = self.expresion[0].run(env)
            cant = self.expresion[1].run(env)

            if(cant['tipo'] == TipoDato.i64):
                contador = cant['valor']
                vec = []
                for i in range(0, contador):
                    vec.append(val['valor'])

                return {'valor': vec, 'tipo': val['tipo']}
            else:
                error = Error("La cantidad de veces a repetir el valor en el vector no es numérica.", "Semántico", self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                return
        else:
            return {'valor': None, 'tipo': TipoDato.error}

    def ast(self):
        pass
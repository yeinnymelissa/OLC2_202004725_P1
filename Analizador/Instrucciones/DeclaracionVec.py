from Analizador.Instrucciones.Instruccion import *
from Analizador.Entorno.Tipo import *
from Analizador.Singleton.Singleton import Singleton
from Analizador.Entorno.Error import *
from Analizador.Entorno.Tipo import *
from datetime import datetime

class DeclaracionVec(Instruccion):
    def __init__(self, nombre, tipo, expresion, editable, tipo_vec, linea, columna):
        self.nombre = nombre
        self.tipo = tipo
        self.expresion = expresion
        self.editable = editable
        self.tipo_vec = tipo_vec
        super().__init__(linea, columna)
    
    def run(self, env):
        singleton = Singleton.getInstance()

        if(self.tipo_vec == TipoVectores.vacio):
            envActual = env.guardar_variable(self.nombre, [], self.tipo, self.editable, TipoSimbolo.vector, self.linea, self.columna)
            if envActual == False:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("Declaración invalida, la variable con el nombre \""+str(self.nombre)+"\" ya existe.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                return
            return
        elif (self.tipo_vec == TipoVectores.valoresIniciales):
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
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("Declaración de vector invalida, los tipos asignados al vector no son del mismo tipo.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                return
            elif bandera == False:
                envActual = env.guardar_variable(self.nombre, vec, tipo[0], self.editable, TipoSimbolo.vector, self.linea, self.columna)
                if envActual == False:
                    now = datetime.now()
                    fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                    error = Error("Declaración invalida, la variable con el nombre \""+str(self.nombre)+"\" ya existe.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                    singleton.addError(error)
                    print(error.descripcion)
                    return
                return
        elif (self.tipo_vec == TipoVectores.repetidos):
             
            val = self.expresion[0].run(env)
            cant = self.expresion[1].run(env)

            if(cant['tipo'] == TipoDato.i64):
                contador = cant['valor']
                vec = []
                for i in range(0, contador):
                    vec.append(val['valor'])

                envActual = env.guardar_variable(self.nombre, vec, val['tipo'], self.editable, TipoSimbolo.vector, self.linea, self.columna)
                if envActual == False:
                    now = datetime.now()
                    fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                    error = Error("Declaración invalida, la variable con el nombre \""+str(self.nombre)+"\" ya existe.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                    singleton.addError(error)
                    print(error.descripcion)
                    return
                return
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("Declaración de vector invalida, la cantidad de veces a repetir el valor no es numérica.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                return
        elif (self.tipo_vec == TipoVectores.capacidad):    
            capa = self.expresion.run(env)

            if(capa['tipo'] == TipoDato.i64):
                vec = []

                for i in range(0, capa['valor']):
                    vec.append(None)

                envActual = env.guardar_variable(self.nombre, vec, self.tipo, self.editable, TipoSimbolo.vector, self.linea, self.columna)
                if envActual == False:
                    now = datetime.now()
                    fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                    error = Error("Declaración invalida, la variable con el nombre \""+str(self.nombre)+"\" ya existe.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                    singleton.addError(error)
                    print(error.descripcion)
                    return
                return
            else:
                now = datetime.now()
                fechaHora = str(now.day) +"/"+str(now.month) +"/"+str(now.year) +" " + str(now.hour) + ":"+ str(now.minute)
                error = Error("Declaración de vector invalida, la capacidad del vector no es numérica.", "Semántico", env.id, fechaHora, self.linea, self.columna)
                singleton.addError(error)
                print(error.descripcion)
                return
            
        return 
    def ast(self):
        pass
        
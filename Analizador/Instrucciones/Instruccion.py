from abc import ABC, abstractmethod

class Instruccion(ABC):
    def __init__(self, linea, columna):
        self.linea = linea
        self. columna = columna
        super().__init__()

        
    @abstractmethod
    def run(self, env):
        pass

    @abstractmethod
    def ast(self):
        pass
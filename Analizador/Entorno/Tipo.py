from __future__ import division
import enum


class TipoSimbolo(enum.Enum):
    variable = 0
    funcion = 1
    modulo = 2

class TipoPrint(enum.Enum):
    expresion = 0
    vec = 1

class TipoDato(enum.Enum):
    error = 0
    i64 = 1
    f64 = 2
    bool = 3
    char = 4
    string = 5
    str = 6

class TipoAritmetica(enum.Enum):
    suma = 0
    resta = 1
    multiplicacion = 2
    division = 3
    powi = 4
    powf = 5
    modulo = 6
    negado = 7

class TipoRelacionales(enum.Enum):
    mayor = 0
    menor = 1
    mayorIgual = 2
    menorIgual = 3
    igualacion = 4
    diferente = 5

class TipoLogicas(enum.Enum):
    OR = 0
    AND = 1
    NOT = 2

global validator

validador = {
    '+': {
        TipoDato.i64: {
            TipoDato.i64: TipoDato.i64,
            TipoDato.f64: TipoDato.f64
        }
    },
    '-': {
        TipoDato.i64: {
            TipoDato.i64: TipoDato.i64,
            TipoDato.f64: TipoDato.f64
        }
    },
    '<': {
        TipoDato.i64: {
            TipoDato.i64: TipoDato.bool,
        },
        TipoDato.f64: {
            TipoDato.f64: TipoDato.bool
        },
    },
    '>': {
        TipoDato.i64: {
            TipoDato.i64: TipoDato.bool,
        },
        TipoDato.f64: {
            TipoDato.f64: TipoDato.bool
        },
    },
    '==': {
        TipoDato.i64: {
            TipoDato.i64: TipoDato.bool,
        },
        TipoDato.f64: {
            TipoDato.f64: TipoDato.bool
        },
    }
}



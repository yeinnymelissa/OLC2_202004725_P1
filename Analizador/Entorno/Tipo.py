import enum


class TipoSimbolo(enum.Enum):
    variable = 0
    funcion = 1
    modulo = 2


class TipoDato(enum.Enum):
    error = 0
    i64 = 1
    f64 = 2
    bool = 3
    char = 4
    string = 5


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



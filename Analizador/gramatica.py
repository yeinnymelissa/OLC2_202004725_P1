reservadas = {
    'true' : 'True',
    'false' : 'False',
    'let': 'Let',
    'mut': 'Mut',
    'i64': 'I64',
    'f64': 'F64',
    'bool': 'Bool',
    '&str': 'String1',
    'String': 'String2',
    'char': 'CharAux'
}

tokens = [
    'Float',
    'Entero',
    'String',
    'Booleano',
    'Char', 
    'Comentario',
    'ptComa',
    'llaveA',
    'llaveC',
    'parA',
    'parC',
    'igual',
    'mas',
    'menos',
    'por',
    'dividido',
    'menorQue',
    'mayorQue',
    'dobleIgual',
    'diferenteQue',
    'dosPuntos',
    'Id'
] + list(reservadas.values())

t_ptComa = r';'
t_llaveA = r'{'
t_llaveC = r'}'
t_parA = r'\('
t_parC = r'\)'
t_igual = r'='
t_mas = r'\+'
t_menos = r'-'
t_por = r'\*'
t_dividido = r'/'
t_menorQue = r'<'
t_mayorQue = r'>'
t_dobleIgual = r'=='
t_diferenteQue = r'!='
t_dosPuntos = r':'

def t_Float(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
        print("Float: "+str(t.value))
    except:
        print("Error al parsear el float.")
    return t

def t_Entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
        print("Entero: "+ str(t.value))
    except:
        print("Error al parsear el entero.")
    return t

def t_String(t):
    r'\".*?\"'
    try:
        t.value = t.value[1:-1]
        print("String: "+t.value)
    except:
        print("Error al parsear el String.")
    return t

def t_Booleano(t):
    r'true|false'
    try:
        if t.value == "true":
            t.value = True
        elif t.value == "false":
            t.value = False
        print("Boolean: "+str(t.value))
    except:
        print("Error al parsear el Booleano.")
    return t

def t_Char(t):
    r'\'.?\''
    try:
        t.value = t.value[1:-1]
        print("Char: "+t.value)
    except:
        print("Error al parsear el Char.")
    return t

def t_Id(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'Id')    # Check for reserved words
     print("ID: "+t.value )
     return t

def t_Comentario(t):
    r'//.*\n'
    print("Comentario")
    t.lexer.lineno += 1

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Error léxico '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

def p_listaInstrucciones(t):
    '''INSTRUCCIONES : INSTRUCCION INSTRUCCIONES
                    | INSTRUCCION'''


def p_Instruccion_Declaracion(t):
    '''INSTRUCCION : DECLARACION'''

def p_Declaracion_Normal(t):
    '''DECLARACION : Let Id igual EXPRESION ptComa'''

def p_Declaracion_Normal_Tipo_I64(t):
    '''DECLARACION : Let Id dosPuntos I64 igual EXPRESION ptComa'''

def p_Declaracion_Normal_Tipo_F64(t):
    '''DECLARACION : Let Id dosPuntos F64 igual EXPRESION ptComa'''

def p_Declaracion_Normal_Tipo_String(t):
    '''DECLARACION : Let Id dosPuntos String1 igual EXPRESION ptComa
                    | Let Id dosPuntos String2 igual EXPRESION ptComa'''

def p_Declaracion_Normal_Tipo_Bool(t):
    '''DECLARACION : Let Id dosPuntos Bool igual EXPRESION ptComa'''

def p_Declaracion_Normal_Tipo_Char(t):
    '''DECLARACION : Let Id dosPuntos CharAux igual EXPRESION ptComa'''

def p_Declaracion_Mut(t):
    '''DECLARACION : Let Mut Id igual EXPRESION ptComa'''    

def p_Declaracion_Mut_Tipo_I64(t):
    '''DECLARACION : Let Mut Id dosPuntos I64 igual EXPRESION ptComa'''

def p_Declaracion_Mut_Tipo_F64(t):
    '''DECLARACION : Let Mut Id dosPuntos F64 igual EXPRESION ptComa'''

def p_Declaracion_Mut_Tipo_String(t):
    '''DECLARACION : Let Mut Id dosPuntos String1 igual EXPRESION ptComa
                    | Let Mut Id dosPuntos String2 igual EXPRESION ptComa'''

def p_Declaracion_Mut_Tipo_Bool(t):
    '''DECLARACION : Let Mut Id dosPuntos Bool igual EXPRESION ptComa'''

def p_Declaracion_Mut_Tipo_Char(t):
    '''DECLARACION : Let Mut Id dosPuntos CharAux igual EXPRESION ptComa'''


#----------------EXPRESION-------------

def p_Expresion_Float(t):
    '''EXPRESION : Float'''

def p_Expresion_Entero(t):
    '''EXPRESION : Entero'''

def p_Expresion_Booleano(t):
    '''EXPRESION : Booleano'''

def p_Expresion_String(t):
    '''EXPRESION : String'''

def p_Expresion_Char(t):
    '''EXPRESION : Char'''

def p_error(t):
    print("Error sintactico '%s'" % t.value)
    t.lexer.skip(1)

import ply.yacc as yacc

parser = yacc.yacc()

def analizar_entrada(entrada):
    parser.parse(entrada)

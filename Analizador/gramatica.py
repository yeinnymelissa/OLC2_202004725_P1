from xml.sax.handler import LexicalHandler
from Analizador.Entorno.Entorno import Entorno
from Analizador.Entorno.Tipo import *
from Analizador.Entorno.Error import Error
from Analizador.Expresiones.Acceso import Acceso
from Analizador.Expresiones.Aritmeticas import Aritmeticas
from Analizador.Expresiones.Literal import Literal
from Analizador.Instrucciones.Asignacion import Asignacion
from Analizador.Instrucciones.Declaracion import Declaracion
from Analizador.Instrucciones.Println import Println
from Analizador.Singleton.Singleton import Singleton

reservadas = {
    'true' : 'True',
    'false' : 'False',
    'let': 'Let',
    'mut': 'Mut',
    'i64': 'I64',
    'f64': 'F64',
    'bool': 'Bool',
    'String': 'StrA',
    'char': 'CharAux',
    'println':'PrintLn',
    'pow':'Powi',
    'powf':'Powf'
}

tokens = [
    'Float',
    'Entero',
    'String',
    'Booleano',
    'Char', 
    'Comentario',
    'ptComa',
    'Coma',
    'llaveA',
    'llaveC',
    'ParA',
    'ParC',
    'igual',
    'mas',
    'menos',
    'por',
    'dividido',
    'modulo',
    'menorQue',
    'mayorQue',
    'menorIgual',
    'mayorIgual',
    'dobleIgual',
    'diferenteQue',
    'dosPuntos',
    'Or',
    'And',
    'Str',
    'not',
    'Id'
] + list(reservadas.values())

t_ptComa = r';'
t_Coma = r','
t_llaveA = r'{'
t_llaveC = r'}'
t_ParA = r'\('
t_ParC = r'\)'
t_Or = r'\|\|'
t_And = r'&&'
t_igual = r'='
t_mas = r'\+'
t_menos = r'-'
t_por = r'\*'
t_dividido = r'/'
t_modulo = r'%'
t_menorQue = r'<'
t_mayorQue = r'>'
t_menorIgual = r'<='
t_mayorIgual = r'>='
t_dobleIgual = r'=='
t_diferenteQue = r'!='
t_dosPuntos = r':'
t_not = r'!'
t_Str = r'&str'

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
     t.type = reservadas.get(t.value,'Id')    # Check for reserved words
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
    singleton = Singleton.getInstance()
    error = Error("El caracter \""+ str(t.value[0]) + "\" no pertenece al lenguaje.", "Léxico", t.lexer.lineno, obtener_columna(t.lexer.lexdata, t))
    singleton.addError(error)
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'Or'),
    ('left', 'And'),
    ('left', 'mas', 'menos'),
    ('nonassoc', 'menorQue', 'mayorQue', 'menorIgual', 'mayorIgual', 'dobleIgual', 'diferenteQue'),  
    ('left', 'por', 'dividido', 'modulo'),
    ('left', 'Powi', 'Powf'),
    ('right', 'not'), 
    ('left', 'UMINUS'),
    ('left', 'UPAR')
)

def p_init(t) :
    'init : INSTRUCCIONES'
    t[0] = t[1]

def p_listaInstrucciones(t):
    '''INSTRUCCIONES : INSTRUCCIONES INSTRUCCION'''
    t[1].append(t[2])
    t[0] = t[1]

def p_listaInstrucciones_Instruccion(t):
    '''INSTRUCCIONES : INSTRUCCION'''
    t[0] = [t[1]]

#-------------DECLARACION---------------

def p_Instruccion_Declaracion(t):
    '''INSTRUCCION : DECLARACION'''
    t[0] = t[1]

def p_Declaracion_Normal(t):
    '''DECLARACION : Let Id igual EXPRESION ptComa'''
    t[0] = Declaracion(t[2], None, t[4], False, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t)) 

def p_Declaracion_Normal_Tipo_I64(t):
    '''DECLARACION : Let Id dosPuntos I64 igual EXPRESION ptComa'''
    t[0] = Declaracion(t[2], TipoDato.i64, t[6], False, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Normal_Tipo_F64(t):
    '''DECLARACION : Let Id dosPuntos F64 igual EXPRESION ptComa'''
    t[0] = Declaracion(t[2], TipoDato.f64, t[6], False, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Normal_Tipo_String(t):
    '''DECLARACION : Let Id dosPuntos StrA igual EXPRESION ptComa'''
    t[0] = Declaracion(t[2], TipoDato.string, t[6], False, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Normal_Tipo_Str(t):
    '''DECLARACION : Let Id dosPuntos Str igual EXPRESION ptComa'''
    t[0] = Declaracion(t[2], TipoDato.str, t[6], False, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Normal_Tipo_Bool(t):
    '''DECLARACION : Let Id dosPuntos Bool igual EXPRESION ptComa'''
    t[0] = Declaracion(t[2], TipoDato.bool, t[6], False, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Normal_Tipo_Char(t):
    '''DECLARACION : Let Id dosPuntos CharAux igual EXPRESION ptComa'''
    t[0] = Declaracion(t[2], TipoDato.char, t[6], False, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Mut(t):
    '''DECLARACION : Let Mut Id igual EXPRESION ptComa'''  
    t[0] = Declaracion(t[3], None, t[5], True, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Mut_Tipo_I64(t):
    '''DECLARACION : Let Mut Id dosPuntos I64 igual EXPRESION ptComa'''
    t[0] = Declaracion(t[3], TipoDato.i64, t[7], True, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Mut_Tipo_F64(t):
    '''DECLARACION : Let Mut Id dosPuntos F64 igual EXPRESION ptComa'''
    t[0] = Declaracion(t[3], TipoDato.f64, t[7], True, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Mut_Tipo_String(t):
    '''DECLARACION : Let Mut Id dosPuntos StrA igual EXPRESION ptComa'''
    t[0] = Declaracion(t[3], TipoDato.string, t[7], True, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Mut_Tipo_Str(t):
    '''DECLARACION : Let Mut Id dosPuntos Str igual EXPRESION ptComa'''
    t[0] = Declaracion(t[3], TipoDato.str, t[7], True, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Mut_Tipo_Bool(t):
    '''DECLARACION : Let Mut Id dosPuntos Bool igual EXPRESION ptComa'''
    t[0] = Declaracion(t[3], TipoDato.bool, t[7], True, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Declaracion_Mut_Tipo_Char(t):
    '''DECLARACION : Let Mut Id dosPuntos CharAux igual EXPRESION ptComa'''
    t[0] = Declaracion(t[3], TipoDato.char, t[7], True, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

#-------------ASIGNACION---------------

def p_Instruccion_Asignacion(t):
    '''INSTRUCCION : ASIGNACION'''
    t[0] = t[1]

def p_Asignacion(t):
    '''ASIGNACION : Id igual EXPRESION ptComa'''
    t[0] = Asignacion(t[1], t[3], t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

#--------------IMPRIMIR----------------

def p_Instruccion_Imprimir(t):
    '''INSTRUCCION : IMPRIMIR'''
    t[0] = t[1]

def p_Imprimir_String(t):
    '''IMPRIMIR : PrintLn not ParA String ParC ptComa'''
    print("IMPRIMIR")
    t[0] = Println(None, t[4], t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Imprimir_String_Comas(t):
    '''IMPRIMIR : PrintLn not ParA String Coma COMASEX ParC ptComa'''
    t[0] = Println(t[4], t[6], t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Comas_Expresion(t):
    '''COMASEX : COMASEX Coma EXPRESION'''
    t[1].append(t[3])
    t[0] = t[1]

def p_Comas_Expre(t):
    '''COMASEX : EXPRESION'''
    t[0] = [t[1]]

#--------------EXPRESION---------------

#-------------ARITMETICAS----------------

def p_Expresion_Suma(t):
    '''EXPRESION : EXPRESION mas EXPRESION'''
    t[0] = Aritmeticas(t[1], t[3], TipoAritmetica.suma, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Resta(t):
    '''EXPRESION : EXPRESION menos EXPRESION'''
    t[0] = Aritmeticas(t[1], t[3], TipoAritmetica.resta, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Multiplicacion(t):
    '''EXPRESION : EXPRESION por EXPRESION'''
    t[0] = Aritmeticas(t[1], t[3], TipoAritmetica.multiplicacion, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Division(t):
    '''EXPRESION : EXPRESION dividido EXPRESION'''
    t[0] = Aritmeticas(t[1], t[3], TipoAritmetica.division, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Modulo(t):
    '''EXPRESION : EXPRESION modulo EXPRESION'''
    t[0] = Aritmeticas(t[1], t[3], TipoAritmetica.modulo, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Negado(t):
    '''EXPRESION : menos EXPRESION %prec UMINUS'''
    t[0] = Aritmeticas(t[2], None, TipoAritmetica.negado, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Par(t):
    '''EXPRESION : ParA EXPRESION ParC %prec UPAR'''
    t[0] = t[2]

def p_Expresion_PowI(t):
    '''EXPRESION : I64 dosPuntos dosPuntos Powi ParA EXPRESION Coma EXPRESION ParC'''
    t[0] = Aritmeticas(t[6], t[8], TipoAritmetica.powi, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Powf(t):
    '''EXPRESION : F64 dosPuntos dosPuntos Powf ParA EXPRESION Coma EXPRESION ParC'''
    t[0] = Aritmeticas(t[6], t[8], TipoAritmetica.powf, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Float(t):
    '''EXPRESION : Float'''
    t[0] = Literal(t[1], TipoDato.f64, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Entero(t):
    '''EXPRESION : Entero'''
    t[0] = Literal(t[1], TipoDato.i64, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Booleano(t):
    '''EXPRESION : Booleano'''
    t[0] = Literal(t[1], TipoDato.bool, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_String(t):
    '''EXPRESION : String'''
    t[0] = Literal(t[1], TipoDato.string, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Char(t):
    '''EXPRESION : Char'''
    t[0] = Literal(t[1], TipoDato.char, t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))

def p_Expresion_Id(t):
    '''EXPRESION : Id'''
    t[0] = Acceso(t[1], t.lineno(1), obtener_columna_p(t.lexer.lexdata, t))



def p_error(t):
    print("Error sintactico '%s'" % t.value)
    singleton = Singleton.getInstance()
    error = Error("El token \""+ str(t.value) + "\" no se esperaba.", "Sintáctico", t.lexer.lineno, obtener_columna(t.lexer.lexdata, t))
    singleton.addError(error)
    print("El token \""+ str(t.value) + "\" no se esperaba.")
    print(t.lexer.lineno)
    print(obtener_columna(t.lexer.lexdata, t))
    t.lexer.skip(1)

def obtener_columna(cadena,token):
    ultimo_salto = cadena.rfind('\n',0,token.lexpos) #determina la posicion inmediatamente anterior del ultimo salto de linea que encuentre en la cadena
    '''
    token.lexpos posicion del primer caracter del token encontrado
    haciendo la resta en el token.lexpos - ultimo_salto se obtiene
    la posicion de la  columna en donde empieza el token
    '''
    columna = (token.lexpos - ultimo_salto)
    return columna

def obtener_columna_p(cadena,token):
    ultimo_salto = cadena.rfind('\n',0,token.lexpos(1)) #determina la posicion inmediatamente anterior del ultimo salto de linea que encuentre en la cadena
    '''
    token.lexpos posicion del primer caracter del token encontrado
    haciendo la resta en el token.lexpos - ultimo_salto se obtiene
    la posicion de la  columna en donde empieza el token
    '''
    columna = (token.lexpos(1) - ultimo_salto)
    return columna

import ply.yacc as yacc

parser = yacc.yacc()

def analizar_entrada(entrada):
    analizador = parser.parse(entrada)

    entornoPadre = Entorno(0, None)
    for instruccion in analizador:
        instruccion.run(entornoPadre)
    
    singleton = Singleton.getInstance()

    print(singleton.getConsola())
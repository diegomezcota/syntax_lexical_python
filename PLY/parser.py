from distutils.log import debug
from msilib.schema import Error
from pexpect import EOF
import ply.yacc as yacc
from lexer import tokens

def p_programa(p):
    '''programa : PROGRAM ID SEMICOLON programa1'''
    #print('programa')
    pass

def p_programa1(p):
    '''programa1    : vars bloque
                    | bloque'''
    #print('programa1')
    pass

def p_vars(p):
    '''vars   : VAR vars1'''
    #print('vars')
    pass

def p_vars1(p):
    '''vars1    : type_def
                | type_def vars1'''
    #print('vars1')

def p_type_def(p):
    '''type_def : ID id_list COLON tipo SEMICOLON'''
    #print('type_def')
    pass

def p_id_list(p):
    '''id_list  : empty
                | COMMA ID id_list'''
    #print('id_list')
    pass

def p_tipo(p):
    '''tipo : INT
            | FLOAT'''
    #print('tipo')
    pass

def p_bloque(p):
    '''bloque   : OPEN_KEY bloque1 CLOSE_KEY'''
    #print('bloque')
    pass

def p_bloque1(p):
    '''bloque1  : empty
                | estatuto bloque1'''
    #print('bloque1')
    pass

def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura'''
    pass

def p_asignacion(p):
    '''asignacion   : ID ASSIGN expresion SEMICOLON'''
    pass

def p_expresion(p):
    '''expresion    : exp expresion1'''
    pass

def p_expresion1(p):
    '''expresion1   : list_comp exp
                    | empty'''
    pass

def p_list_comp(p):
    '''list_comp    : LESS_THAN
                    | GREATER_THAN
                    | NOT_EQUAL'''
    pass

def p_escritura(p):
    '''escritura    : PRINT OPEN_PARENTHESIS print_arg escritura1 CLOSE_PARENTHESIS SEMICOLON'''
    pass

def p_escritura1(p):
    '''escritura1   : COMMA print_arg escritura1
                    | empty'''
    pass

def p_print_arg(p):
    '''print_arg    : expresion
                    | CTE_STRING'''
    pass

def p_condicion(p):
    '''condicion    : IF OPEN_PARENTHESIS expresion CLOSE_PARENTHESIS bloque condicion1 SEMICOLON'''
    pass

def p_condicion1(p):
    '''condicion1   : ELSE bloque
                    | empty'''
    pass

def p_exp(p):
    '''exp  : termino exp1'''
    pass

def p_exp1(p):
    '''exp1 : exp2 exp1
            | empty'''
    pass

def p_exp2(p):
    '''exp2 : PLUS termino
            | MINUS termino'''
    pass

def p_termino(p):
    '''termino  : factor termino1'''
    pass

def p_termino1(p):
    '''termino1 : termino2 factor termino1
                | empty'''
    pass

def p_termino2(p):
    '''termino2 : PRODUCT
                | DIVISION'''
    pass

def p_factor(p):
    '''factor   : var_cte
                | OPEN_PARENTHESIS expresion CLOSE_PARENTHESIS
                | factor1 var_cte'''
    pass

def p_factor1(p):
    '''factor1  : PLUS
                | MINUS'''
    pass

def p_var_cte(p):
    '''var_cte  : CTE_OR
                | ID
                | CTE_ARROW_UP'''
    pass

def p_empty(p):
    '''empty :'''
    #print('empty')
    pass

class SyntaxError(Exception):
    pass

def p_error(p):
    print('syntax error', p)
    raise SyntaxError
    
parser = yacc.yacc()

test_files = ['test1.in', 'test2.in', 'test3.in', 'test4.in']

for i, test in enumerate(test_files):
    try:
        s = open('tests/' + test, 'r').read()
        parser.parse(s)
        print('test no.', i + 1, ': apropiado')
    except SyntaxError:
        print('There was a syntax error in test. no', i + 1)
    except EOFError:
        break
    

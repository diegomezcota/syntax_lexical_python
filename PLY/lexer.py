# ------------------------------------------------------------
# lexer.py
#
# tokenizer for language expression evaluator
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
'SEMICOLON',
'COMMA',
'COLON',
'OPEN_KEY',
'CLOSE_KEY',
'ASSIGN',
'GREATER_THAN',
'LESS_THAN',
'NOT_EQUAL',
'OPEN_PARENTHESIS',
'CLOSE_PARENTHESIS',
'PLUS',
'MINUS',
'PRODUCT',
'DIVISION',
'ID',
'INT_VALUE',
'FLOAT_VALUE',
'STRING_VALUE'
]

# Regular expression rules for simple tokens
t_SEMICOLON         = r';'
t_COMMA             = r','
t_COLON             = r'\:'
t_OPEN_KEY          = r'{'
t_CLOSE_KEY         = r'}'
t_ASSIGN            = r'='
t_GREATER_THAN      = r'>'
t_LESS_THAN         = r'<'
t_NOT_EQUAL         = r'<>'
t_OPEN_PARENTHESIS  = r'\('
t_CLOSE_PARENTHESIS = r'\)'
t_PLUS              = r'\+'
t_MINUS             = r'-'
t_PRODUCT           = r'\*'
t_DIVISION          = r'/'

# Reserved words
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'int' : 'INT',
    'float' : 'FLOAT',
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'print' : 'PRINT'
}

tokens += list(reserved.values())

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# ID check for reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_FLOAT_VALUE(t):
    r'[0-9]+\.[0-9]+(E[\+-]?[0-9]+)?'
    t.type = reserved.get(t.value, 'FLOAT_VALUE')
    return t

def t_INT_VALUE(t):
    r'[0-9]+'
    t.type = reserved.get(t.value, 'INT_VALUE')
    return t

def t_STRING_VALUE(t):
    r'".*"'
    t.type = reserved.get(t.value, 'STRING_VALUE')
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
)

# dictionary of names
names = {}

# Test it out
data = '''
10.01
0.01
10.0E-9
100000
"hola que show"
"ff213904u1fs,f//fsd"
'''

# print("---PROBANDO ANALIZADOR LÉXICO---")
# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)
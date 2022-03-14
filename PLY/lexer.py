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
'ID'
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
    'print' : 'PRINT',
    'cte_string' : 'CTE_STRING',
    'cte_or' : 'CTE_OR',
    'cte_arrow_up' : 'CTE_ARROW_UP'
}

tokens += list(reserved.values())

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# ID check for reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
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
program a00824758;
var a, b, c : int;
if (a < b) {
    print(cte_string);
    print(cte_or);
    print(cte_arrow_up);
} else {
    print(a);
}
'''

# print("---PROBANDO ANALIZADOR LÉXICO---")
# Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)
    
# print("---PROBANDO ANALIZADOR SINTÁCTICO---")
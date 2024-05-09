from ply import lex

reserved = {
    'for': 'FOR',
    'if': 'IF',
    'do': 'DO',
    'while': 'WHILE',
    'else': 'ELSE',
}

tokens = [
    'ID',
    'LPAREN',
    'RPAREN',
] + list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
from ply import lex
from difflib import SequenceMatcher


reserved = {
    'for': 'FOR',
    'if': 'IF',
    'do': 'DO',
    'while': 'WHILE',
    'else': 'ELSE',
    'programa': 'PROGRAMA'  
}

tokens = [
    'ID',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'COMMA',
    'LBRACE',
    'RBRACE',
    'ERROR'  
] + list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_LBRACE = r'\{'
t_RBRACE = r'\}'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    elif similar_to_reserved(t.value):
        t.type = 'ERROR'
    else:
        t.type = 'ID'
    return t

def similar_to_reserved(word):
    for reserved_word in reserved:
        if SequenceMatcher(None, word, reserved_word).ratio() > 0.8:
            return True
    return False

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

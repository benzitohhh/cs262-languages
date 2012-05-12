# Wes Weimer
# -- STUDENTS WRITE this file 
#
# This is a set of regular expressions defining a lexer for JavaScript
# fragments. 
#
# Students would be expected to write this file. They would be given a
# list of all of the tokens, an English description of the associated set
# of strings, and a name for the token.
#
# Tricky Bits:
# Handling non-nested /* comments */
# Tracking Newlines
#

import ply.lex as lex

tokens = (
    'ANDAND', # &&
    'COMMA', # ,
    'DIVIDE', # /
    'ELSE', # else
    'EQUAL', # =
    'EQUALEQUAL', # ==
    'FALSE', # false
    'FUNCTION', # function
    'GE', # >=
    'GT', # >
    'IDENTIFIER', # factorial
    'IF', # if
    'LBRACE', # {
    'LE', # <=
    'LPAREN', # (
    'LT', # <
    'MINUS', # -
    'MOD', # %
    'NOT', # !
    'NUMBER', # 1234 5.678
    'OROR', # ||
    'PLUS', # +
    'RBRACE', # }
    'RETURN', # return
    'RPAREN', # )
    'SEMICOLON', # ;
    'STRING', # "this is a \"tricky\" string"
    'TIMES', # *
    'TRUE', # TRUE
    'VAR', # var 
)

states = (
    ('comment', 'exclusive'), # /* ... */ 
)

def t_comment(t):
    r'\/\*'
    t.lexer.begin('comment')

def t_comment_end(t):
    r'\*\/'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    pass

def t_comment_error(t):
    t.lexer.skip(1)

def t_eolcomment(t):
    r'//.*'
    pass

reserved = [ 'function', 'if', 'var', 'return', 'else', 'true', 'false' ]

def t_IDENTIFIER(t):
    r'[A-Za-z][A-Za-z_]*'
    if t.value in reserved:
        t.type = t.value.upper()
    return t

def t_NUMBER(t):
    r'-?[0-9]+(\.[0-9]*)?'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|(\\.))*"'
    t.value = t.value[1:-1] # strip off "
    return t

t_ANDAND = r'&&'
t_COMMA = r','
t_DIVIDE = r'/'
t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_LPAREN = r'\('
t_LBRACE = r'{'
t_RBRACE = r'}'
t_SEMICOLON = r';'
t_MINUS = r'-'
t_MOD = r'%'
t_NOT = r'!'
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_RPAREN = r'\)'
t_TIMES = r'\*'
t_LE = r'<='
t_LT = r'<'
t_GT = r'>'
t_GE = r'>='

t_ignore = ' \t\v\r'
t_comment_ignore = ' \t\v\r'

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print "JavaScript Lexer: Illegal character " + t.value[0]
    t.lexer.skip(1)

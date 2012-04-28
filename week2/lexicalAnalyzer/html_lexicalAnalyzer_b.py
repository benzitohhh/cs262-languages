import ply.lex as lex

tokens = (
	'LANGLE',		# <
	'LANGLESLASH',	# </
	'RANGLE',		# >
	'EQUAL',		# =
	'STRING',		# "hello"
	'WORD',			# Welcome!
)


states = (
	('htmlcomment', 'exclusive'),
)

t_ignore = ' '		# shortcut for whitespace


#--------------------
# non token-returning definitions
#

def t_htmlcomment(token):
	r'<!--'
	token.lexer.begin('htmlcomment') # switch mode

def t_htmlcomment_end(token):
	r'-->'
	token.lexer.lineno += token.value.count('\n') # hack to add newlines in comment to global linecount
	token.lexer.begin('INITIAL') # switch back to default mode

def t_htmlcomment_error(token):
	token.lexer.skip(1) # pass

def t_newline(token):
	r'\n'
	token.lexer.lineno += 1
	pass


#--------------------
# token-returning definitions
#

def t_LANGLESLASH(token):
	r'</'
	return token

def t_LANGLE(token):
	r'<'
	return token

def t_RANGLE(token):
	r'>'
	return token

def t_EQUAL(token):
	r'='
	return token

def t_STRING(token):
	r'"[^"]*"'
	token.value = token.value[1:-1]
	return token

def t_WORD(token):
	r'[^ <>\n]+'
	return token

webpage = "hello <!-- commend --> all"
htmllexer = lex.lex()
htmllexer.input(webpage)
while True:
	tok = htmllexer.token()
	if not tok: break
	print tok



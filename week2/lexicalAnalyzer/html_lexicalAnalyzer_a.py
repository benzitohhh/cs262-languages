import ply.lex as lex

tokens = (
	'LANGLE',		# <
	'LANGLESLASH',	# </
	'RANGLE',		# >
	'EQUAL',		# =
	'STRING',		# "hello"
	'WORD',			# Welcome!
)

t_ignore = ' '		# shortcut for whitespace

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
	r'[^ <>]+'
	return token

# webpage = '"This" is <b>my</b> webpage!'
htmllexer = lex.lex()
webpage = """Tricky "string" <i>output</i>!"""
htmllexer.input(webpage)
while True:
	tok = htmllexer.token()
	if not tok: break
	print tok



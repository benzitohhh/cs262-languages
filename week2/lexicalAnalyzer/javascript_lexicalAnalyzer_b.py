import ply.lex as lex

tokens = (
	'NUMBER',
	'IDENTIFIER',		# "hello"
)

t_ignore = ' '		# shortcut for whitespace


#--------------------
# non token-returning definitions
#

def t_eolcomment(token):
	r'//[[\n]]*'
	pass
	

#--------------------
# token-returning definitions
#

def t_IDENTIFIER(token):
	r'[a-zA-Z][a-zA-Z_]*]'
	return token

def t_NUMBER(token):
	r'-?[0-9]+(:?\.[0-9]*)'
	token.value = float(token.value)
	return token

inputcode = "6"
jslexer = lex.lex()
jslexer.input(inputcode)
while True:
	tok = jslexer.token()
	if not tok: break
	print tok



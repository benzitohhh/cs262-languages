# Expanding Exp
# This is very, very difficult.

grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]

def expand(tokens, grammar): # input tokens (the product of each re-write)
    "Exands a single phrase"
    for pos in range(len(tokens)):
        for rule in grammar:
            if tokens[pos] == rule[0]:
                yield tokens[0:pos] + rule[1] + tokens[pos+1:]
             
depth = 5
utterances = [["exp"]] # start symbol
for x in range(depth):
    for sentence in utterances:
        utterances = utterances + [ i for i in expand(sentence, grammar)]

for sentence in utterances:
    print " ".join(sentence)
    
#    ['exp']
#    ['exp', '+', 'exp']
#    ['exp', '-', 'exp']
#    ['(', 'exp', ')']
#    ['num']

# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x87\xdb\x1a\x83l\r\xaa\xec\xd3\xbcf\xb6\xa3]j\x94'
    
_lr_action_items = {'RPAREN':([2,4,5,6,7,9,10,],[-2,-4,-3,-6,9,-1,-5,]),'NUMBER':([0,4,8,],[2,2,2,]),'COMMA':([2,6,9,],[-2,8,-1,]),'LPAREN':([3,],[4,]),'IDENTIFIER':([0,4,8,],[3,3,3,]),'$end':([1,2,9,],[0,-2,-1,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'args':([4,8,],[5,10,]),'exp':([0,4,8,],[1,6,6,]),'optargs':([4,],[7,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> IDENTIFIER LPAREN optargs RPAREN','exp',4,'p_exp_call','/home/benimmanuel/Desktop/cs262-languages/week4/javaScriptParsing1.py',61),
  ('exp -> NUMBER','exp',1,'p_exp_number','/home/benimmanuel/Desktop/cs262-languages/week4/javaScriptParsing1.py',65),
  ('optargs -> args','optargs',1,'p_optargs','/home/benimmanuel/Desktop/cs262-languages/week4/javaScriptParsing1.py',69),
  ('optargs -> <empty>','optargs',0,'p_optargs_empty','/home/benimmanuel/Desktop/cs262-languages/week4/javaScriptParsing1.py',73),
  ('args -> exp COMMA args','args',3,'p_args','/home/benimmanuel/Desktop/cs262-languages/week4/javaScriptParsing1.py',77),
  ('args -> exp','args',1,'p_args_last','/home/benimmanuel/Desktop/cs262-languages/week4/javaScriptParsing1.py',80),
]

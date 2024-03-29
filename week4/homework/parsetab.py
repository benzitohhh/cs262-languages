
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xe9Eb\xc95\x07\xb6\x8d\xef\x10j\xe3\xb68t8'
    
_lr_action_items = {'OROR':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,10,-1,-4,10,-6,-7,-8,-9,-12,-18,-14,-17,-11,-13,-15,-10,-16,10,-19,]),'ANDAND':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,11,-1,-4,11,-6,-7,11,-9,-12,-18,-14,-17,-11,-13,-15,-10,-16,11,-19,]),'GT':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,12,-1,-4,12,-6,-7,12,12,-12,-18,-14,-17,-11,-13,-15,12,-16,12,-19,]),'FALSE':([0,4,6,10,11,12,13,14,15,16,17,18,19,20,22,39,],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]),'STRING':([0,4,6,10,11,12,13,14,15,16,17,18,19,20,22,39,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'$end':([1,2,3,5,7,8,21,23,24,25,26,27,28,29,30,31,32,33,34,38,],[-5,-3,-2,0,-1,-4,-6,-7,-8,-9,-12,-18,-14,-17,-11,-13,-15,-10,-16,-19,]),'LT':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,16,-1,-4,16,-6,-7,16,16,-12,-18,-14,-17,-11,-13,-15,16,-16,16,-19,]),'NUMBER':([0,4,6,10,11,12,13,14,15,16,17,18,19,20,22,39,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'TIMES':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,15,-1,-4,15,-6,-7,15,15,15,-18,15,-17,15,15,15,15,15,15,-19,]),'GE':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,14,-1,-4,14,-6,-7,14,14,-12,-18,-14,-17,-11,-13,-15,14,-16,14,-19,]),'LE':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,17,-1,-4,17,-6,-7,17,17,-12,-18,-14,-17,-11,-13,-15,17,-16,17,-19,]),'PLUS':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,18,-1,-4,18,-6,-7,18,18,18,-18,18,-17,18,18,-15,18,-16,18,-19,]),'LPAREN':([0,4,6,7,10,11,12,13,14,15,16,17,18,19,20,22,39,],[4,4,4,22,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'NOT':([0,4,6,10,11,12,13,14,15,16,17,18,19,20,22,39,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'RPAREN':([1,2,3,7,8,9,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,],[-5,-3,-2,-1,-4,23,-6,-20,-7,-8,-9,-12,-18,-14,-17,-11,-13,-15,-10,-16,38,-21,-23,-19,-22,]),'EQUALEQUAL':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,19,-1,-4,19,-6,-7,19,19,-12,-18,-14,-17,-11,-13,-15,-10,-16,19,-19,]),'IDENTIFIER':([0,4,6,10,11,12,13,14,15,16,17,18,19,20,22,39,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'TRUE':([0,4,6,10,11,12,13,14,15,16,17,18,19,20,22,39,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'MINUS':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,20,-1,-4,20,-6,-7,20,20,20,-18,20,-17,20,20,-15,20,-16,20,-19,]),'COMMA':([1,2,3,7,8,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,-1,-4,-6,-7,-8,-9,-12,-18,-14,-17,-11,-13,-15,-10,-16,39,-19,]),'DIVIDE':([1,2,3,5,7,8,9,21,23,24,25,26,27,28,29,30,31,32,33,34,37,38,],[-5,-3,-2,13,-1,-4,13,-6,-7,13,13,13,-18,13,-17,13,13,13,13,13,13,-19,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'args':([22,39,],[36,40,]),'exp':([0,4,6,10,11,12,13,14,15,16,17,18,19,20,22,39,],[5,9,21,24,25,26,27,28,29,30,31,32,33,34,37,37,]),'optargs':([22,],[35,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> IDENTIFIER','exp',1,'p_exp_identifier','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',127),
  ('exp -> NUMBER','exp',1,'p_exp_number','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',131),
  ('exp -> STRING','exp',1,'p_exp_string','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',135),
  ('exp -> TRUE','exp',1,'p_exp_true','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',139),
  ('exp -> FALSE','exp',1,'p_exp_false','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',143),
  ('exp -> NOT exp','exp',2,'p_exp_not','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',147),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_exp_parens','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',151),
  ('exp -> exp OROR exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',171),
  ('exp -> exp ANDAND exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',172),
  ('exp -> exp EQUALEQUAL exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',173),
  ('exp -> exp LT exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',174),
  ('exp -> exp GT exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',175),
  ('exp -> exp LE exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',176),
  ('exp -> exp GE exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',177),
  ('exp -> exp PLUS exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',178),
  ('exp -> exp MINUS exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',179),
  ('exp -> exp TIMES exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',180),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_binop','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',181),
  ('exp -> IDENTIFIER LPAREN optargs RPAREN','exp',4,'p_exp_func_call','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',186),
  ('optargs -> <empty>','optargs',0,'p_optargs_empty','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',190),
  ('optargs -> args','optargs',1,'p_optargs','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',194),
  ('args -> exp COMMA args','args',3,'p_args','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',198),
  ('args -> exp','args',1,'p_args_single','/home/benimmanuel/Desktop/cs262-languages/week4/homework/5.py',202),
]

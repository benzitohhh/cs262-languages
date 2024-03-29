
# parsetabhtml.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'g\xd1\x96v\\d\x11\xa8i\x12u\x14\x87\xb7\x1a\x83'
    
_lr_action_items = {'LANGLE':([0,2,3,4,5,6,14,15,24,],[1,-3,-5,-14,-4,1,-8,1,-9,]),'WORD':([0,1,2,3,4,5,6,8,9,13,14,15,16,19,20,21,24,],[2,8,-3,-5,-14,-4,2,-6,12,12,-8,2,19,-12,-13,22,-9,]),'STRING':([0,2,3,4,5,6,14,15,16,24,],[3,-3,-5,-14,-4,3,-8,3,20,-9,]),'JAVASCRIPT':([0,2,3,4,5,6,14,15,24,],[4,-3,-5,-14,-4,4,-8,4,-9,]),'EQUAL':([0,2,3,4,5,6,12,14,15,24,],[5,-3,-5,-14,-4,5,16,-8,5,-9,]),'SLASHRANGLE':([8,9,11,13,17,19,20,],[-6,-11,14,-11,-10,-12,-13,]),'RANGLE':([8,9,11,13,17,19,20,22,23,],[-6,-11,15,-11,-10,-12,-13,-7,24,]),'LANGLESLASH':([2,3,4,5,6,10,14,15,18,24,],[-3,-5,-14,-4,-2,-1,-8,-2,21,-9,]),'$end':([0,2,3,4,5,6,7,10,14,24,],[-2,-3,-5,-14,-4,-2,0,-1,-8,-9,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'tag_arguments':([9,13,],[11,17,]),'tag_argument':([9,13,],[13,13,]),'tagnameend':([21,],[23,]),'element':([0,6,15,],[6,6,6,]),'html':([0,6,15,],[7,10,18,]),'tagname':([1,],[9,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> html","S'",1,None,None,None),
  ('html -> element html','html',2,'p_html','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',15),
  ('html -> <empty>','html',0,'p_html_empty','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',18),
  ('element -> WORD','element',1,'p_element_word','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',22),
  ('element -> EQUAL','element',1,'p_element_word_eq','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',26),
  ('element -> STRING','element',1,'p_element_word_string','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',30),
  ('tagname -> WORD','tagname',1,'p_tagname','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',34),
  ('tagnameend -> WORD','tagnameend',1,'p_tagnameend','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',40),
  ('element -> LANGLE tagname tag_arguments SLASHRANGLE','element',4,'p_element_tag_empty','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',49),
  ('element -> LANGLE tagname tag_arguments RANGLE html LANGLESLASH tagnameend RANGLE','element',8,'p_element_tag','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',56),
  ('tag_arguments -> tag_argument tag_arguments','tag_arguments',2,'p_tag_arguments','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',61),
  ('tag_arguments -> <empty>','tag_arguments',0,'p_tag_arguments_empty','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',65),
  ('tag_argument -> WORD EQUAL WORD','tag_argument',3,'p_tag_argument_word','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',69),
  ('tag_argument -> WORD EQUAL STRING','tag_argument',3,'p_tag_argument_string','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',73),
  ('element -> JAVASCRIPT','element',1,'p_element_javascript','/Users/immanuel_ben/Desktop/cs262-languages/week6/homework/htmlgrammar.py',77),
]

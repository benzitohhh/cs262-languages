# represent as tuples:   (left_child, content, right_child)
# no child? use None
import pprint

def insert(tree, element):
    # base case - insert into an empty tree
    if tree == None:
        return (None, element, None)
    else:
        # recursively update
        left_child, this_element, right_child = tree
        if element <= this_element:
            new_left_child = insert(left_child, element)
            return (new_left_child, this_element, right_child)
        else:
            new_right_child = insert(right_child, element)
            return (left_child, this_element, new_right_child)

def contains(tree, element):
    if tree == None:
        return False
    else:
        left_child, this_element, right_child = tree
        if this_element == element:
            return True
        elif element <= this_element:
            return contains(left_child, element)
        else:
            return contains(right_child, element)

elements = [2,4,16,13, 19, 24]
t = insert(None, 5)
for e in elements:
    t = insert(t, e)
    pprint.pprint(t)
   
print
print contains(t, 5)
for e in elements:
    print "contains(t, " + str(e) + ") = ", contains(t, e)
for e in [77,44,22]:
    print "contains(t, " + str(e) + ") = ", contains(t, e)
    
  

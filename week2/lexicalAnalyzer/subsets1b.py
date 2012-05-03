# Bonus Practice: Subsets

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.

def all_sublists(big_list):
	print sublists(big_list, [])

def sublists(big_list, selected_so_far):
	# base case
	if big_list == []:
		return [selected_so_far]
	else:
		 current_element = big_list[0]
		 rest_of_big_list = big_list[1:]
		 return sublists(rest_of_big_list, selected_so_far + [current_element]) + \
		 		sublists(rest_of_big_list, selected_so_far)

dinner_guests = ["a", "b", "c"]		 
all_sublists(dinner_guests)
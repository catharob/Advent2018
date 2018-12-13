"""
This is day 2, part 2 of Advent of Code, 2018.
"""
import sys

sample_data = [
"abcdet",
"fghijt",
"klmnot",
"pqrstt",
"fguijt",
"axcyet",
"wvxyzt",
"fehirt"
]

import difflib as d
import ast

def find_matching_strings(stringone, stringtwo):
	"""This function uses the difflib library to find strings that match within two longer strings."""
	matches = d.SequenceMatcher(None, stringone, stringtwo).get_matching_blocks()
	desired_output = []
	for match in matches:
		thing = "[%d, %d, %d]" % match
		thing = ast.literal_eval(thing)
		desired_output.append(thing)
	del desired_output[-1]
	return desired_output

def compare_list_to_single_word(word, list):
	"""This function compares one string to a list of strings to find one that matches with just one letter difference."""
	for item in list:
		n = find_matching_strings(word, item)
		if len(n) == 2 and (n[0][2]+n[1][2]) == (len(word) - 1):
			return word, item

def pop_one_list_item_out_to_compare(data, index):
	"""This function extracts one item from a list (so it can be prepared to be compared to the rest of the list items."""
	word = data[index]
	newlist = data
	del data[index]
	return word, newlist

def put_it_all_together(data):
	"""This function brings it all together - popping each item in the list out and comparing the rest of the list to it, in order to find the one almost-matching pair."""
	for item in data:
		n = pop_one_list_item_out_to_compare(data, data.index(item))
		m = compare_list_to_single_word(n[0], n[1])
		if not m == None:
			return m

a = put_it_all_together(data)
print a

# I manually compared the words, because I ran out of steam.
# Here was the output once I ran the put_it_all_together function.
# ('jbbenqtlagxhivmwyscjukztdp', 'jbbenqtlavxhivmwyscjukztdp')
# Solution:
# jbbenqtlaxhivmwyscjukztdp

sys.exit()






















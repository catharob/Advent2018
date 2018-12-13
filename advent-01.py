"""
This is day 1, part 2 of Advent of Code, 2018. (I didn't add part 1, as the solution, a sum, seemed trivial.)
"""

import sys

sample_changes = [1, -2, 3, 1]

def getfreq(list, freq):
	freqs = []
	for x in list:
		freq += x
		freqs.append(freq)

	return freqs

def contfreq(x):
	startfreq = 0
	freqs = []
	a = 0
	while a < 200:
		y = getfreq(x, startfreq)
		for freq in y:
			if freq not in freqs:
				freqs.append(freq)
			else:
				print freq
				break
		startfreq = y[-1]
		a += 1
		
contfreq(sample_changes)


sys.exit()



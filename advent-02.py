"""
This is day 2, part 1 of Advent of Code, 2018.
"""

import sys

# lines of code to convert raw data to useful list
# with open('data-advent-02.py') as input_file:
#     print ','.join(['"{}"'.format(line.rstrip('\n')) for line in input_file])


alphabet = "abcdefghijklmnopqrstuvwxyz" # gotta remember to get all the letters in there, friendo
sample_data = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
sample_data2 = ["cppp", "zzzz", "qesv", "shkr", "njgs", "kvvb", "rmyn"]

data = ["jplenqtlagxhivmwmscfukzodp","jbrehqtlagxhivmeyscfuvzodp","jbreaqtlagxzivmwysofukzodp","jxrgnqtlagxhivmwyscfukwodp","jbrenqtwagjhivmwysxfukzodp","jbrenqplagxhivmwyscfuazoip","jbrenqtlagxhivzwyscfldzodp","jbrefqtlagxhizmwyfcfukzodp","jbrenqtlagxhevmwfsafukzodp","jbrunqtlagxrivmsyscfukzodp","jbrenqtlaguhivmwyhlfukzodp","jbrcnstsagxhivmwyscfukzodp","jbrenqtlagozivmwyscbukzodp","jbrenqwlagxhivswysrfukzodp","jbrenstlagxhuvmiyscfukzodp","jbranqtlhgxhivmwysnfukzodp","jbrenqtvagxhinmxyscfukzodp","jbrenqtlagdhivmwyscfukxody","jbrenqtlagelavmwyscfukzodp","jbrenqtlagxhtvmwyhcfukzbdp","jbrenqwlagxhivmwyscfutzopp","jbrenqtlavxhibmtyscfukzodp","jbronqtlagxnivmwyscfuzzodp","jbredqtlagxhppmwyscfukzodp","jbrcnqtlogxhivmwysxfukzodp","jbremqtlagehivswyscfukzodp","jbrenqolagxhivmcyscfukzokp","jbrehqtlacxhgvmwyscfukzodp","fbrlnqtlagxhivmwyscbukzodp","zbrfnqtlagxhivrwyscfukzodp","jbregqtlagxnivmwyscfhkzodp","jbrenqtllgxnivmwystfukzodp","jurenqtlagxhivmwyscfulzoup","jbrenitdagxhivmwyxcfukzodp","jbrenqtlagxqivmwyscvuszodp","jbqenqwlagxhivmwyscfckzodp","jbrenqtlagxhivmwxscqupzodp","jbrenqtlagxhivmwysciuqiodp","jbrjnjtlagxhivmwyscfukzode","jbrenqtlagxhuvmwqscfukzods","jbrenqtlagxhuvmuyscfukzudp","ibrenqtlagxhivmwyscfuktokp","jbsenqtlagxhivcwyscfuksodp","jbrfnntlagxhivmwnscfukzodp","jzrenqulagxhivmwyscfukzodx","jbrenqtqygxhivmwyscfukzwdp","jbrenqtlagxfixmwyscfukzcdp","jbrenqaoagxhivmwyshfukzodp","jbrenqtlazxhivmworcfukzodp","jbrenqtlagxhicowyscfukrodp","jbrqnqtlagxhivzwyzcfukzodp","jbrenqtlalxhuvxwyscfukzodp","jbrenqtlqgxhhviwyscfukzodp","jbrenqtuggxhivmoyscfukzodp","jbrenqtlagxpivmwyscfukkodw","zbrenqhlagxhivmwyscdukzodp","jbrenutlagxxivmwyscfukzoqp","obrenqtlagxhivmwxscfuszodp","jbrenqtlagxhlvmwyscfuixodp","rbrenqtlagdhixmwyscfukzodp","jbrenqtlagxhivmwescfyszodp","jbrfnqtlagxhivmwyscaukzhdp","jbrenqtiagxhivmbyscfuxzodp","cbrrnqtuagxhivmwyscfukzodp","jbkenqtlagxhigmwysufukzodp","jbjewqtlagxhivmwyscfuqzodp","jbrznqtlagxvivmwyscfukzovp","jbrenttlacxhivmwyscfhkzodp","jblenqtlagxhivmwylcfukaodp","jbrenqtlagxhivmqysiftkzodp","jbrenqtlagwhikmwyscfukqodp","jbrenqtlegxhivmwvsckukzodp","jbrenqwzagxhiamwyscfukzodp","jbrenqtlagxhivcwyscfgkzodc","jbrenqtlagxxhvmwxscfukzodp","jbrenqtlngxhivmwyscfukoowp","jbreomtlagxhivmwpscfukzodp","jfrenqtlagxhivmwyscnumzodp","jbrenqtlagphipmwyscfukfodp","jvrenqtlagxhivmwyscfmkzodw","jbrenqtlaxxoiemwyscfukzodp","jbrenqtlagxhivmwyscemkzpdp","jbrenyjldgxhivmwyscfukzodp","jbrenqtlagxhivfvyspfukzodp","kbrenctlakxhivmwyscfukzodp","jbrmhqtlagxhivmwyscfuizodp","jbjenqtlagxlivmbyscfukzodp","jbrenqtlaaxhivmmyshfukzodp","jbronqtlagxhirmvyscfukzodp","jbcrnqtlagxwivmwyscfukzodp","jxrenszlagxhivmwyscfukzodp","jbpenqtlagxhivmwyscfukkody","jbrewqtlawxhivmwyscfukzhdp","jbrenqylagxhivmwlxcfukzodp","jbrenqtlagxxivtwywcfukzodp","jbrenqtlagxhcvgayscfukzodp","jbrenitlagxhivmwiscfukzohp","jbrenutlagxhivmwyscbukvodp","nbrenqtlagxhivmwysnfujzodp","jbrenqtlagxhivmwyqcfupzoop","jbrenqtrarxhijmwyscfukzodp","jbrenqtlagxhivmwysdfukzovy","jbrrnqtlagxhivmwyvcfukzocp","jbrenqtlagxhivmwyscfuvzzhp","jbhenitlagxhivmwysufukzodp","jbrenqtlagxhivmwyscfuwzoqx","kbrenqtlagxhivmwysqfdkzodp","jbrenqtlagxhivmwyxmfukzodx","jbcenatlagxxivmwyscfukzodp","jbrenhtlagvhdvmwyscfukzodp","jxrenqtlafxhivfwyscfukzodp","jbreaztlpgxhivmwyscfukzodp","tqrenqtlagxfivmwyscfukzodp","jbrenqgllgxhwvmwyscfukzodp","jbrejjtlagxhivmgyscfukzodp","jbrenqtlagxhivmwyscvukzoqv","jbrvnqtlagxsibmwyscfukzodp","jbrenqttagxhuvmwyscfukvodp","jbrenqteagxhivmwcscfukqodp","jbrenqtsabxhivmwyspfukzodp","jbbenqtlagxhivmwyscjukztdp","jnrenqtlagxhiimwydcfukzodp","jbrenqtlagxhfvmwyscxukzodu","jbrenqtluyxhiomwyscfukzodp","jbrenqvlagxhivmwyscuukzolp","ebrenqtlagxnivmwysrfukzodp","jbreeqtlatxhigmwyscfukzodp","jbrenqtvxgxhivmwyscfukzedp","jbrmnqtlagxhivmwywcfuklodp","jbreeqtvagxhivmwyscfukzody","jbrenptlagxhivmxyscfumzodp","jbrenqtlagxhivmwysgfukzfsp","jurenqtlagjhivmwkscfukzodp","jbrenntlagxhivmwtscffkzodp","jbrenqglagxhivmwyocfokzodp","wbrenqtlagxhivmwhscfukiodp","jbrenqtligxhivmqascfukzodp","jbrenqtlagxhivmwxscfukpojp","jurenqtlagxhivmmyscfbkzodp","jbrenqtmagxhivmwyscfrbzodp","jcrenqtlagxhivmwysefukzodm","jbrenqtlagxhicmwywcfukzodl","jbvanqtlagfhivmwyscfukzodp","jbmenqjlagxhivmwyscfdkzodp","jbrenqtlagohivvwysctukzodp","jbrenqtdagxdivmwyscfckzodp","kbrefqtlagxhivmwyscfuazodp","jbrwnqtoagxhivmwyswfukzodp","jjhenqtlagxhivmwyscfukzorp","jbgsnqtlagxhivkwyscfukzodp","jbrynqtlagxhivmsyspfukzodp","jbrenftlmkxhivmwyscfukzodp","nbrenqtxagxhmvmwyscfukzodp","jbrunqtlagxhijmwysmfukzodp","jbrenqtlagmaivmwyscfukzowp","jbrerqtlagxhihmwyscfukzudp","jbrenqtlagahivmwysckukzokp","kbrenqtlagxhirmwyscfupzodp","jbrrnqtlagxhivmwyecfukzodz","jbrenqtlavxhivmwyscfusiodp","jnrenqtlagxhivmwyhcfukzodw","jbretqtlagfhivmwyscfukzrdp","jbreoqtnagxhivmwyscfukzopp","jbrenbtllgxhivmwsscfukzodp","jbrenqtlmgxhivmwyscfuwzedp","jbnenqtlagxhivbwyscfukzokp","jbrenqslagxhivmvyscfukzndp","jbrenqtlagxzivmwuscfukztdp","gbrenqtlagxhyvmwyscfukjodp","jbrenqteagxhivmwyscfuszedp","jbrenqtlaglhivmwysafukkodp","jbrenqtlagxhcvmwascfukzogp","jbrenqtlagxhsvmkcscfukzodp","jbrenqslbgxhivmwyscfufzodp","cbrenqtlagxhivkwtscfukzodp","jbrenqtltgxhivmzyscfukzodj","jbrgnqtlagihivmwyycfukzodp","vbrenqauagxhivmwyscfukzodp","jbrqnqtlagjhivmwyscfqkzodp","jbrenqtlakxhivmwyscfukvobp","jcrenqelagxhivmwtscfukzodp","jbrrnqtlagxhlvmwyscfukzodw","jbrenqtlagxhivmwkscaumzodp","jbrenqdlagxhivmiescfukzodp","jhrenqtlagxhqvmwyscmukzodp","jbrenqtlaghhivmwyscfukkoyp","jowenqtlagxyivmwyscfukzodp","jbrenitaagxhivmwyscfqkzodp","jbrenqtlagxhivmwyscfnkbudp","jbyenqtlagxhivmiyscfukzhdp","jbrenitlagxhibjwyscfukzodp","jbrenqtlavxhjvmwpscfukzodp","jbrenqyaagxhivmwyscflkzodp","jbrenqylagxhivmwyicfupzodp","jbrenqtlagxmevmwylcfukzodp","lbrenqtlagxhiqmwyscfikzodp","jbrenqtnarxhivmwyscfmkzodp","jbrenqtlamxhivmwyscfnkzorp","jbbenqtlavxhivmwyscjukztdp","jbrenqtlagxhivmwyscfnliodp","jbwenetlagxhivmwyscfukzodt","jbrenatlagxhivmwysmfujzodp","jbrsnstlagxhivmwyscfukgodp","jbwvnitlagxhivmwyscfukzodp","jbrenqtbagxhkvmwypcfukzodp","jbrlnqtlafxhivmwyscfukdodp","jbrenztlanxhivmwyscjukzodp","jbrepqtlagxhivmwudcfukzodp","jbrenqtlagxiivmwdscfskzodp","jbrdjqtlagxhivmwyschukzodp","jbrenqtoaguhivmwyccfukzodp","jdrexqjlagxhivmwyscfukzodp","jbrenqtlagxhovmwysckukaodp","pbrfnqblagxhivmwyscfukzodp","jbrenqtlagxrivgiyscfukzodp","jbrelqtgagxhivmryscfukzodp","jbrenqtlagxhicmwjscfikzodp","jbrenqjlagxhivmwyscfmkjodp","jbrenqtlagxpivmwzscgukzodp","jbienqzlagxpivmwyscfukzodp","jbrenqvlagxhivmwdscfukzodx","owrenqtlagxhivmwyicfukzodp","gbrenqtlaathivmwyscfukzodp","jbgenqtlafxhivmwysqfukzodp","jbrenqtlagxhivtwsscfukzokp","jbrnnqylanxhivmwyscfukzodp","ebrenqolagxhivmcyscfukzodp","jbrenqtlarnhivgwyscfukzodp","jbmenqtlagxhivmvyscfukzgdp","jbrevqtlaglhivmwystfukzodp","jbrenqplanthivmwyscfukzodp","jbrenqtlagxhivmkyscbukzosp","jbrenqtlagxaivmwyscfugzodo","jbrenqplagxhnvmwyscfjkzodp","jbrenqtlagxhivgwyscfusrodp","cbrenqtlagxhivmwysmfukzody","jbrenquwaexhivmwyscfukzodp","jbredqtlagxhdvmwyscfukzoup","jbrxnqtlagxhivmwysczukaodp","jbrenqtlafnhivmwyscfuczodp","jbbdkqtlagxhivmwyscfukzodp","ubrenqtlagxhivkwyucfukzodp","ebjenqtlagxhivmwyscfukzodj","jbgenqtlugxxivmwyscfukzodp","jbrenqtoagxqivmwdscfukzodp","bbeenqtlagxhivmwyscfumzodp","jbfeeqtlagxhivmwmscfukzodp","jbrlnqtlagxhiimwescfukzodp","jbrenqtlagwoivmwyscfukhodp","jbrenqtlagnhivmwyscfuszovp"]


def count_letters(word, char):
	count = 0
	for c in word:
		if char == c:
			count += 1
	return count

def dict_for_word(word):
	dict1 = {}
	for letter in alphabet:
		count = count_letters(word, letter)
		if count == 2 or count == 3:
			dict1[letter] = count
	return dict1

def dict_of_dicts(data):
	dict2 = {}
	for word in data:
		dict2[word] = dict_for_word(word)
	return dict2

y = dict_of_dicts(data)
print y

def count_of_three(dictofdicts):
	count_of_three = 0
	for key in dictofdicts:
		vals = list(dictofdicts[key].values())
		if 3 in vals:
			count_of_three += 1
	return count_of_three

def count_of_two(dictofdicts):
	count_of_two = 0
	for key in dictofdicts:
		vals = list(dictofdicts[key].values())
		if 2 in vals:
			count_of_two += 1
			# print vals
	return count_of_two

def calibrate(a, b):
	return a*b

a = count_of_three(y)
print a

b = count_of_two(y)
print b

c = calibrate(a, b)
print c

sys.exit()


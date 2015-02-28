import string
import hashlib
import sys

"""We break this hash the same way we break all hashes, by performing a reverse lookup"""

HASH = "0AB1A9222A15DA1159EB94212C5C8BAF".lower()

for n1 in range(0, 100):
	for letter in list(string.ascii_lowercase):
		for n2 in range(0, 1000):
			string1 = str(n1) + letter + str(n2)
			m = hashlib.md5()
			m.update(string1)
			if m.hexdigest() == HASH:
				print string1
				sys.exit()

"flag: 15q478"

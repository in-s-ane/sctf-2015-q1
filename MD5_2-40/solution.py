import string
import hashlib
import sys
import itertools

"""We break this hash the same way we break all hashes, by performing a reverse lookup"""

HASH = "2E561F52DF1F1A31B5C4A00D0C846728".lower()
alphanum = string.ascii_lowercase + string.digits

for length in range(2, 8):
	print length
	for i in itertools.product(alphanum, repeat=length):
		string1 = "".join(i)
		m = hashlib.md5()
		m.update(string1)
		if m.hexdigest() == HASH:
			print string1
			sys.exit()

"""This takes quite a while... An easier way is to use one of the gigantic hash-databses
online for a lookup, one example is the infamous hashkiller
http://www.hashkiller.co.uk/md5-decrypter.aspx"""

"flag: 581qq92"

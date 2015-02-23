# creds to Richard for realizing that slashes can be represented as binary

import binascii

f = open("slashes.txt", "r")
stream = f.read()
stream_bin = stream.replace("/", "0").replace("\\", "1")
n = int(stream_bin, 2)
output = binascii.unhexlify('%x' % n)

stream_bin = output.replace("\\", "0").replace("/", "1")
n = int(stream_bin, 2)
output = binascii.unhexlify('%x' % n)

stream_bin = output.replace("/", "0").replace("\\", "1")
n = int(stream_bin, 2)
output = binascii.unhexlify('%x' % n)

stream_bin = output.replace("\\", "0").replace("/", "1")
n = int(stream_bin, 2)
output = binascii.unhexlify('%x' % n)

print output

import codecs

flag_file = "server.py"
plaintext = ""

x = 0

for i in flag_file:
    x *= 7
    x += 98

for c in flag_file[::-1]:
    l = ord(c)
    i = chr((l - x) % 256)
    plaintext += i
    x -= 98
    x //= 7

print codecs.encode(plaintext[::-1], 'hex')

# Flag: obfuscated_python_is_definitely_legit

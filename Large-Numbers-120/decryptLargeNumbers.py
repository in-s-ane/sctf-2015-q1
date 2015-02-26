'''
Since the numbers used to encrypt the message are so large, the rounding error
introduced by the integer conversion should not have much of an effect on the
ciphertext. As a result, we can try to work backwords using the ciphertext and
what we know about how the ciphertext is generated.
First, we notice that n is just the string of ascii representations of each
character in the ciphertext. The algorithm then iterates through n and replaces
each 0 digit with repr(int(z/9999)) and each non-zero digit with repr(int(z/int(h)*999))
Then, all the 'L' characters resulting from the repr() of a long are replaced
with _, giving us a convenient way to split the ciphertext into characters.
Finally, the trailing '_' is removed.

First, we can split up our ciphertext into separate lines by the _ delimiter and
then sort the lines. Looking at the sorted output, we see that a few lines are
multiple magnitudes of 10 smaller than others. This is because when we encounter a 0
digit during encryption, the long represented by the z variable is divided by
9999 while otherwise the long is divided by int(h) and multiplied by 999,
which should change the magnitude of the product by at most 1 magitude of 10.
Therefore, we know that the smallest number in the
ciphertext,
"165325052323522887184523906391691283647648112207443516848596141639379234974597120L"
represents a 0 digit in the ascii representation. We can then recover an
approximate value for z by multiplying this by 9999 to get,
"1653085198182905348958054540010521145192833473962227724969112820252152970510996602880L"
Multiplying this by 999 will allow us to calculate the value of h in
"repr(int(z/int(h)*999))" Now all we have to do is read the ciphertext numbers
lines by line and perform the simple calculation to recover the string n,
"108961141031019510210598111110969999105" Then, we split up the string into
groups of 2-3 digits so we can convert these ascii numbers into text. Notice
we can split this string into numbers in the high 90s and low 100s, placing us
in the alphabetical range of the ascii table. Our conversion gives us the string
'l`rge_fibon`cci' which we can infer to be 'large_fibonacci' by accounting for
rounding errors introduced by the float to integer conversion ('`' is right below
'a' on the ascii table)

'''

#z ~= 1653085198182905348958054540010521145192833473962227724969112820252152970510996602880L
#z * 999 ~= 1651432112984722443609096485470510624047640640488265497244143707431900817540485606277120L

zTimes999 = 1651432112984722443609096485470510624047640640488265497244143707431900817540485606277120L

f = open('largeNumbers.txt', 'r')
lines = f.readlines()
plaintext = ""
for line in lines:
    line = long(line.strip())
    if line == 165325052323522887184523906391691283647648112207443516848596141639379234974597120L:
        plaintext += '0'
    else:
        plaintext += str(zTimes999 / line)

print plaintext
# 108 96 114 103 101 95 102 105 98 111 110 96 99 99 105
# l`rge_fibon`cci
# large_fibonacci

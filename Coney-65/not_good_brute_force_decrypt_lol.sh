while read line; do 
    PASS=$line

    openssl aes-128-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
    if [ $? -eq 0 ]; then cat decrypted.txt; fi
    openssl aes-128-ecb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
    if [ $? -eq 0 ]; then cat decrypted.txt; fi
    openssl aes-192-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
    if [ $? -eq 0 ]; then cat decrypted.txt; fi
    openssl aes-192-ecb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
    if [ $? -eq 0 ]; then cat decrypted.txt; fi
    openssl aes-256-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
    if [ $? -eq 0 ]; then cat decrypted.txt; fi
    openssl aes-256-ecb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
    if [ $? -eq 0 ]; then cat decrypted.txt; fi
    openssl des -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
    if [ $? -eq 0 ]; then cat decrypted.txt; fi
    openssl des-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
    if [ $? -eq 0 ]; then cat decrypted.txt; fi
done < /usr/share/dict/words
___='
openssl cast -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl cast-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl cast5-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl cast5-cfb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl cast5-ecb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl cast5-ofb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-cfb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ecb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ede -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ede-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ede-cfb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ede-ofb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ede3 -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ede3-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ede3-cfb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ede3-ofb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des-ofb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl des3 -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl desx -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl rc2 -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl rc2-40-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl rc2-64-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl rc2-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl rc2-cfb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl rc2-ecb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl rc2-ofb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl rc4 -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl rc4-40 -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl seed -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl seed-cbc -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl seed-cfb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl seed-ecb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
openssl seed-ofb -d -a -salt -in x -out decrypted.txt -k $PASS > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then cat decrypted.txt; fi
'

PASS=date

openssl aes-128-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl aes-128-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl aes-192-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl aes-192-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl aes-256-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl aes-256-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl base64 -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl bf -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl bf-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl bf-cfb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl bf-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl bf-ofb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl camellia-128-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl camellia-128-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl camellia-192-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl camellia-192-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl  -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl camellia-256-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl camellia-256-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl cast -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl cast-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl cast5-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl cast5-cfb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl cast5-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl cast5-ofb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-cfb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ede -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ede-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ede-cfb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ede-ofb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ede3 -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ede3-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ede3-cfb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ede3-ofb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des-ofb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl des3 -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl desx -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl rc2 -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl rc2-40-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl rc2-64-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl rc2-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl rc2-cfb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl rc2-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl rc2-ofb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl rc4 -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl rc4-40 -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl seed -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl seed-cbc -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl seed-cfb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl seed-ecb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"
openssl seed-ofb -d -in DecodedBase64.bin -out decrypted.txt -k $PASS
cat decrypted.txt; echo "\n"

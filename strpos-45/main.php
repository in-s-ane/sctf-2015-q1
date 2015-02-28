
<!--

CODE BACKUP ©SCTF CORPORATION EVEN THO WE AINT A CORPORATION:

$a = $_GET["plang"];
if(isset($a)) {
	if(strpos($a,"answer") !== false && strlen($a) < 2) {
		echo $flag;
	} else {
		echo "Sadly, yee hath given bad input.";
	}
}

-->
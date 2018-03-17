<html>
<body>

<?php
//On recupere la valeur de gpio et de value
$Kill = $_GET["kill"];
$processName = "Cam101";


if($Kill == 1)
    exec(escapeshellcmd('pkill -f Cam101'));
else{
    $command = escapeshellcmd(' -a Cam101 /usr/custom/test.py');
    $output = shell_exec($command);
    echo $output;
    exec($command);
}


?>

</body>
</html>

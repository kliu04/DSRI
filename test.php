<?php
// outputs the username that owns the running php/httpd process
// (on a system with the "whoami" executable in the path)
$output=null;
$retval=null;
exec('M2 --script solve_all.m2 x^2+y^2+z^2 > solutions.txt', $output, $retval);
echo "Returned with status $retval and output:\n";
print_r($output);

debug_print_backtrace()
?>

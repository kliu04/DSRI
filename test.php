<?php
if ($_GET['run']) {
  # This code will run if ?run=true is set.
  echo shell_exec("bash run.sh x^2+y^2+z^2-1");
}
?>

<!-- This link will add ?run=true to your URL, myfilename.php?run=true -->
<a href="?run=true">Click Me!</a>

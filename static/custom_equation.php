<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $eqn = $_POST["equation"];

    // Display the submitted data
    echo "Eqn: " . $eqn . "<br>";


    $type = $_POST['type'];  

    echo "Type: " . $type . "<br>";

    if ($type == "2D")
    {
        echo "A";
        // echo shell_exec("python3 ../math/2D_solvers/wrapper.py " . $eqn);
        echo shell_exec("python3 ../test.py");

        // echo shell_exec("ls");

        echo "B";
        // echo __FILE__;
    }
    else {
        echo "3D is not currently supported.";
    }
}
?>

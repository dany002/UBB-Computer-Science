<?php
$servername = "172.17.0.2";
$username = "root";
$password = "password";
$dbname = "personschannelsphpdb";
$dbport = "3306";
$conn = mysqli_connect($servername, $username, $password, $dbname, $dbport);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
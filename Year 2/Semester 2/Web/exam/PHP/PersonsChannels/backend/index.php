<?php
global $conn;
include 'database.php';
session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Forum</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="ajax.js"></script>
    <style>
        .login {
            font-size: 40px;

        }

        .container{
            margin-top: 300px;
            margin-left: 500px;
        }
    </style>
</head>

<body>

<div class="container">
    <p id="success"></p>

    <label>
        <input id="login_user" type="text" placeholder="Username" class="login">
    </label>
    <button id = "login_btn" class="login">Login</button>
</div>

</body>

</html>

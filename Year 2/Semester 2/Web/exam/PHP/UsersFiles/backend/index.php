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
            margin-left: 200px;
        }
    </style>
</head>

<body>

<div class="container">
    <p id="success"></p>
    <div>
        <label>
            <input id="register_user" type="text" placeholder="Username" class="login">
            <input id="register_password" type="text" placeholder="Password" class="login">
        </label>
        <button id= "register_btn" class="login">Register</button>
    </div>
</div>
<div class="container">
    <div>
        <label>
            <input id="login_user" type="text" placeholder="Username" class="login">
            <input id="login_password" type="text" placeholder="Password" class="login">
        </label>
        <button id = "login_btn" class="login">Login</button>
    </div>
</div>

</body>

</html>

<?php
global $conn;
include 'database.php';
session_start();


if (count($_POST) > 0){
    if($_POST['type'] == 1){
        $user = $_POST["username"];
        $password = $_POST["password"];

        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        $stmt = $conn->prepare("INSERT INTO Users(username, password) VALUES (?,?)");
        $stmt->bind_param("ss", $user, $hashedPassword);
        if ($stmt->execute()) {
            echo json_encode(array("statusCode" => 200));
        } else {
            echo json_encode(array("statusCode" => 404, "message" => "User found"));
        }

        $stmt->close();
        $conn->close();
    }
}

if (count($_POST) > 0){
    if($_POST['type'] == 2){
        $user = $_POST["username"];
        $password = $_POST["password"];


        $stmt = $conn->prepare("SELECT * FROM Users WHERE username=?");
        $stmt->bind_param("s", $user);

        if ($stmt->execute()) {
            $result = $stmt->get_result();
            $row = $result->fetch_assoc();
            if (password_verify($password, $row["password"])) {
                $_SESSION['user'] = $row;
                echo json_encode(array("statusCode" => 200, "user" => $row));
            } else {
                echo json_encode(array("statusCode" => 404, "message" => "User not found"));
            }
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
        $conn->close();
    }
}
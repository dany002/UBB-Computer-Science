<?php
global $conn;
include 'database.php';
session_start();


if (count($_POST) > 0){
    if($_POST['type'] == 1){
        $user = $_POST["username"];
        $_SESSION['user'] = $user;
        echo json_encode(array("statusCode" => 200));
    }
}

if (count($_POST) > 0){
    if($_POST['type'] == 2){
        $topicname = $_POST["topic"];
        $text = $_POST["text"];

        $stmt = $conn->prepare("SELECT * FROM Topics WHERE topicname = ?");
        $stmt->bind_param("s",$topicname);
        if($stmt->execute()){
            $result = $stmt->get_result();
            $row = $result->fetch_assoc();

            if($row){ // that means we have a topic
                $id = $row["id"];
                $username = $_SESSION['user'];
                $stmt = $conn->prepare("INSERT INTO Posts(user,topicId,text,date) VALUES(?,?,?,NOW())");
                $stmt->bind_param("sis",$username, $id, $text);
                if($stmt->execute()){
                    echo json_encode(array("statusCode" => 200));
                }
                else{
                    echo json_encode(array("statusCode" => 400));
                }
            }
            else{
                $stmt = $conn->prepare("INSERT INTO Topics(topicname) VALUES(?)");
                $stmt->bind_param("s",$topicname);
                if($stmt->execute()){
                    $stmt = $conn->prepare("SELECT id FROM Topics WHERE topicname = ?");
                    $stmt->bind_param("s",$topicname);
                    if($stmt->execute()){
                        $result = $stmt->get_result();
                        $row = $result->fetch_assoc();
                        $username = $_SESSION['user'];
                        $stmt = $conn->prepare("INSERT INTO Posts(user,topicId,text,date) VALUES(?,?,?,NOW())");
                        $stmt->bind_param("sis",$username, $row, $text);
                        if($stmt->execute()){
                            echo json_encode(array("statusCode" => 200));
                        }
                        else{
                            echo json_encode(array("statusCode" => 401));
                        }
                    }
                    else{
                        echo json_encode(array("statusCode" => 402));
                    }
                }
                else{
                    echo json_encode(array("statusCode" => 403));
                }
            }
        } else{
            echo json_encode(array("statusCode" => 404));
        }

    }
}
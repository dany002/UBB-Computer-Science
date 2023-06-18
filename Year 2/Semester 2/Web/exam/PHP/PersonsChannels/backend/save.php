<?php
global $conn;
include 'database.php';
session_start();

if (count($_POST) > 0){
    if($_POST['type'] == 1){
        $user = $_POST["username"];
        $stmt = $conn->prepare("SELECT * FROM Persons WHERE name = ?");
        $stmt->bind_param("s", $user);
        if ($stmt->execute()) {
            $result = $stmt->get_result();
            $row = $result->fetch_assoc();
            if ($row) {
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


if (count($_POST) > 0 && $_POST['type'] == 2) {
    $owner = $_POST["owner"];

    // Prepare the SQL query
    $query = "SELECT * FROM Channels WHERE ownerid = (SELECT id FROM Persons WHERE name = ?)";
    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $owner);

    if ($stmt->execute()) {
        $result = $stmt->get_result();
        $channels = array();

        while ($row = $result->fetch_assoc()) {
            $channels[] = $row;
        }

        echo json_encode($channels);
    } else {
        echo json_encode(array("error" => "Query execution failed"));
    }

    $stmt->close();
    $conn->close();
}


if (count($_POST) > 0 && $_POST['type'] == 3) {
    $user = $_SESSION["user"]["name"];

    // Prepare the SQL query with a parameterized query
    $query = "SELECT * FROM Channels WHERE subscribers LIKE CONCAT('%', ?, '%')";
    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $user);

    if ($stmt->execute()) {
        $result = $stmt->get_result();
        $channels = array();

        while ($row = $result->fetch_assoc()) {
            $channels[] = $row;
        }

        echo json_encode($channels);
    } else {
        echo json_encode(array("error" => "Query execution failed"));
    }

    $stmt->close();
    $conn->close();
}


if (count($_POST) > 0 && $_POST['type'] == 4) {
    $user = $_SESSION["user"]["name"];

    // Prepare the SQL query
    $query = "UPDATE Channels
              SET subscribers =
                  CONCAT(
                      CASE
                          WHEN subscribers LIKE CONCAT('%', ?, ' -> %') THEN
                              CONCAT(
                                  SUBSTRING_INDEX(subscribers, CONCAT(?, ' -> '), 1),
                                  CONCAT(?, ' -> ', DATE_FORMAT(NOW(), '%d/%m/%Y')),
                                  SUBSTRING_INDEX(SUBSTRING_INDEX(subscribers, CONCAT(?, ' -> '), -1), '. ', -1)
                              )
                          ELSE
                              subscribers
                      END,
                      CASE
                          WHEN subscribers NOT LIKE CONCAT('%', ?, '%') THEN
                              CONCAT( ?, ' -> ', DATE_FORMAT(NOW(), '%d/%m/%Y'), '. ')
                          ELSE
                              ''
                      END
                  )
              WHERE subscribers LIKE CONCAT('%', ?, '%') OR subscribers NOT LIKE CONCAT('%', ?, '%')";

    $stmt = $conn->prepare($query);
    $stmt->bind_param("ssssssss", $user, $user, $user, $user, $user, $user, $user, $user);



    if ($stmt->execute()) {
        echo json_encode(array("statusCode" => 200, "row" => $row));
    } else {

        echo json_encode(array("error" => "Update failed"));
    }

    $stmt->close();
    $conn->close();
}

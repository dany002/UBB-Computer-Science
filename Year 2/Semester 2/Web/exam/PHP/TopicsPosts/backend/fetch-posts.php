<?php
global $conn;
session_start();
include 'database.php';

$result = mysqli_query($conn, "SELECT * FROM Posts");
$i = 1; // Start index for the displayed rows
$rows = array();
while ($row = mysqli_fetch_array($result)) {
    $id = $row["topicid"];
    $secondresult = mysqli_query($conn, "SELECT topicname FROM Topics WHERE id=$id");
    $secondrow = mysqli_fetch_array($secondresult);

    $rows[] = array(
        'id' => $row["id"],
        'user' => $row["user"],
        'topic' => $secondrow["topicname"],
        'text' => $row["text"],
        'date' => $row["date"]
    );

    $i++;
}

echo json_encode($rows);
?>
<?php

global $conn;
include 'database.php';


if (count($_POST) > 0 && $_POST['type'] == 1) {
    $query = "SELECT * FROM City";
    $stmt = $conn->prepare($query);

    if ($stmt->execute()) {
        $result = $stmt->get_result();
        $cities = array();

        while ($row = $result->fetch_assoc()) {
            $cities[] = $row;
        }

        echo json_encode($cities);
    } else {
        echo json_encode(array("error" => "Query execution failed"));
    }

    $stmt->close();
    $conn->close();
}

if (count($_POST) > 0 && $_POST['type'] == 2) {

    $id = $_POST["id"];

    $stmt = $conn->prepare("SELECT Link.*, City1.name AS city1_name, City2.name AS city2_name FROM Link 
        INNER JOIN City AS City1 ON Link.idCity1 = City1.id 
        INNER JOIN City AS City2 ON Link.idCity2 = City2.id 
        WHERE Link.idCity1 = ? OR Link.idCity2 = ?
        ORDER BY 0.6 * Link.duration + 0.4 * Link.distance");



    $stmt->bind_param("ii", $id, $id);
    if ($stmt->execute()) {
        $result = $stmt->get_result();
        $links = array();

        while ($row = $result->fetch_assoc()) {
            $links[] = $row;
        }

        echo json_encode($links);
    } else {
        echo json_encode(array("error" => "Query execution failed"));
    }

}
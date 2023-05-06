<?php
include 'database.php';

if (count($_POST) > 0) {
    if ($_POST['type'] == 1) {
        $author = $_POST["author"];
        $title = $_POST["title"];
        $pages = $_POST["pages"];
        $types = $_POST["types"];
        $format = $_POST["format"];

        $stmt = $conn->prepare("INSERT INTO Document (author, title, pages, types, format) VALUES (?, ?, ?, ?, ?)");
        $stmt->bind_param("ssiss", $author, $title, $pages, $types, $format);

        if ($stmt->execute()) {
            echo json_encode(array("statusCode" => 200));
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
        $conn->close();
    }
}

if (count($_POST) > 0) {
    if ($_POST['type'] == 2) {
        $id = $_POST['id'];
        $author = $_POST["author"];
        $title = $_POST["title"];
        $pages = $_POST["pages"];
        $types = $_POST["types"];
        $format = $_POST["format"];

        $stmt = $conn->prepare("UPDATE Document SET author = ?, title = ?, pages = ?, types = ?, format = ? WHERE id = ?");
        $stmt->bind_param("ssissi", $author, $title, $pages, $types, $format, $id);

        if ($stmt->execute()) {
            echo json_encode(array("statusCode" => 200));
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
        $conn->close();
    }
}

if (count($_POST) > 0) {
    if ($_POST['type'] == 3) {
        $id = $_POST['id'];

        $stmt = $conn->prepare("DELETE FROM Document WHERE id = ?");
        $stmt->bind_param("i", $id);

        if ($stmt->execute()) {
            echo $id;
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
        $conn->close();
    }
}

if (count($_POST) > 0) {
    if ($_POST['type'] == 4) {
        $id = $_POST['id'];

        $stmt = $conn->prepare("DELETE FROM Document WHERE id IN ($id)");

        if ($stmt->execute()) {
            echo $id;
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
        $conn->close();
    }
}
?>

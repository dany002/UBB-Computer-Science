<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: access");
header("Access-Control-Allow-Methods: PUT");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

$method = $_SERVER['REQUEST_METHOD'];

if ($method == "OPTIONS") {
    die();
}

if ($_SERVER['REQUEST_METHOD'] !== 'PUT') :
    http_response_code(405);
    echo json_encode([
        'success' => 0,
        'message' => 'Bad Request detected! Only PUT method is allowed',
    ]);
    exit;
endif;

require 'db_connect.php';
$database = new Operations();
$conn = $database->dbConnection();

$data = json_decode(file_get_contents("php://input"));
$id = isset($_GET['id']) ? $_GET['id'] : null;


if ($id == null) {
    echo json_encode(['success' => 0, 'message' => 'Please enter correct Documents id.']);
    exit;
}

try {
    $fetch_post = "SELECT * FROM Document WHERE id=:id";
    $fetch_stmt = $conn->prepare($fetch_post);
    $fetch_stmt->bindValue(':id', $id, PDO::PARAM_INT);
    $fetch_stmt->execute();
    //echo "HI";
    if ($fetch_stmt->rowCount() > 0) :
        $row = $fetch_stmt->fetch(PDO::FETCH_ASSOC);
        $author = isset($data->author) ? $data->author : $row['author'];
        $title = isset($data->title) ? $data->title : $row['title'];
        $pages = isset($data->pages) ? $data->pages : $row['pages'];
        $types = isset($data->types) ? $data->types : $row['types'];
        $format = isset($data->format) ? $data->format : $row['format'];

        $stmt = $conn->prepare("UPDATE Document SET author = ?, title = ?, pages = ?, types = ?, format = ? WHERE id = ?");

        $stmt->bindParam(1, $author);
        $stmt->bindParam(2, $title);
        $stmt->bindParam(3, $pages);
        $stmt->bindParam(4, $types);
        $stmt->bindParam(5, $format);
        $stmt->bindParam(6, $id);

        if (empty(trim($data->author)) || empty(trim($data->title)) || empty(trim($data->pages)) || empty(trim($data->types)) || empty($data->format)) {
            http_response_code(400);
            echo json_encode([
                'success' => 0,
                'message' => 'Field cannot be empty. Please fill all the fields.',
            ]);
            exit;
        }

        if ($stmt->execute()) {
            echo json_encode([
                'success' => 1,
                'message' => 'Record updated successfully'
            ]);
            exit;
        }

        echo json_encode([
            'success' => 0,
            'message' => 'Did not update. Something went  wrong.'
        ]);
        exit;

    else :
        echo json_encode(['success' => 0, 'message' => 'Invalid ID. No record found by the ID.']);
        exit;
    endif;
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode([
        'success' => 0,
        'message' => $e->getMessage()
    ]);
    exit;
}

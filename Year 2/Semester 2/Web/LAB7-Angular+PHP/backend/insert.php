<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: access");
header("Access-Control-Allow-Methods: POST");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

$method = $_SERVER['REQUEST_METHOD'];

if ($method == "OPTIONS") {
    die();
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') :
    http_response_code(405);
    echo json_encode([
        'success' => 0,
        'message' => 'Bad Request!.Only POST method is allowed',
    ]);
    exit;
endif;

require 'db_connect.php';
$database = new Operations();
$conn = $database->dbConnection();

$data = json_decode(file_get_contents("php://input"));


if (!isset($data->author) || !isset($data->title) || !isset($data->pages) || !isset($data->types) || !isset($data->format)):
    http_response_code(400);
    echo json_encode([
        'success' => 0,
        'message' => 'Please enter compulsory fileds |  Author, Title, Pages, Types, Format',
    ]);
    exit;

elseif (empty(trim($data->author)) || empty(trim($data->title)) || empty(trim($data->pages)) || empty(trim($data->types)) || empty($data->format)) :
    http_response_code(400);
    echo json_encode([
        'success' => 0,
        'message' => 'Field cannot be empty. Please fill all the fields.',
    ]);
    exit;

endif;

try {

    $author = $data->author;
    $title = $data->title;
    $pages = $data->pages;
    $types = $data->types;
    $format = $data->format;


    $stmt = $conn->prepare("INSERT INTO Document (author, title, pages, types, format) VALUES (?, ?, ?, ?, ?)");
    $stmt->bindParam(1, $author);
    $stmt->bindParam(2, $title);
    $stmt->bindParam(3, $pages);
    $stmt->bindParam(4, $types);
    $stmt->bindParam(5, $format);


    if ($stmt->execute()) {

        http_response_code(201);
        echo json_encode([
            'success' => 1,
            'message' => 'Data Inserted Successfully.'
        ]);
        exit;
    }

    echo json_encode([
        'success' => 0,
        'message' => 'There is some problem in data inserting'
    ]);
    exit;

} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode([
        'success' => 0,
        'message' => $e->getMessage()
    ]);
    exit;
}
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
    echo json_encode([
        'success' => 0,
        'message' => 'Please enter compulsory fileds |  Author, Title, Pages, Types, Format',
    ]);
    exit;

elseif (empty(trim($data->author)) || empty(trim($data->title)) || empty(trim($data->pages)) || empty(trim($data->types)) || empty($data->format)) :

    echo json_encode([
        'success' => 0,
        'message' => 'Field cannot be empty. Please fill all the fields.',
    ]);
    exit;

endif;

try {
    $author = htmlspecialchars(trim($data->first_name));
    $title = htmlspecialchars(trim($data->last_name));
    $pages = htmlspecialchars(trim($data->email));
    $types = htmlspecialchars(trim($data->password));
    $format = htmlspecialchars(trim($data->format));

    #TODO SQL INJECTION
    $query = "INSERT INTO Document(
    author
    title,
    pages,
    types,
    format
    ) 
    VALUES(
    :author,
    :title,
    :pages,
    :types,
    :format
    )";

    $stmt = $conn->prepare($query);

    $stmt->bindValue(':author', $author, PDO::PARAM_STR);
    $stmt->bindValue(':title', $title, PDO::PARAM_STR);
    $stmt->bindValue(':pages', $pages, PDO::PARAM_STR);
    $stmt->bindValue(':types', $types, PDO::PARAM_STR);
    $stmt->bindValue(':format', $format, PDO::PARAM_STR);

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
<?php
class Operations
{
    private $db_host = '172.17.0.2';
    private $db_name = 'newdb';
    private $db_username = 'root';
    private $db_password = 'password';
    private $db_port = "3306";

    public function dbConnection()
    {
        try {
            $conn = new PDO('mysql:host=' . $this->db_host . ';dbname=' . $this->db_name, $this->db_username, $this->db_password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            return $conn;
        } catch (PDOException $e) {
            echo "Connection error " . $e->getMessage();
            exit;
        }
    }
}
<?php
global $conn;
session_start();
include 'database.php';


if (!isset($_SESSION['user'])) {
    // Redirect the user to another page or display an error message
    header("Location: index.php"); // Replace "login.php" with the appropriate page
    exit(); // Terminate the script to prevent further execution
}

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Forum</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="ajax.js"></script>

    <style>



        .container {
            justify-content: center;
            align-items: flex-start;
            margin-top: 50px;
        }


        table {
            width: 100%;
            border-collapse: collapse;
        }

        table th,
        table td {
            padding: 10px;
            text-align: left;
            border: 1px solid #ddd;
        }

        table th {
            background-color: #f2f2f2;
        }
    </style>
</head>

<body>

<div class="container">
    <div>
    <label>
        <input id="topic_name_input" type="text" placeholder="Topic name">
        <input id="post_text_input" type="text" placeholder="Post text">
    </label>
        <button id="topic_name_btn" type="button">Add Post</button>
    </div>
    <table>
        <thead>
        <tr>
            <th>ID</th>
            <th>User</th>
            <th>Topicid</th>
            <th>Text</th>
            <th>Date</th>
        </tr>
        </thead>
        <tbody>
        <?php
        $result = mysqli_query($conn,"SELECT * FROM Posts");

        $i = 1; // Start index for the displayed rows
        while ($row = mysqli_fetch_array($result)) {
            ?>
            <tr id="<?php echo $row["id"]; ?>">
                <td><?php echo $i; ?></td>
                <td><?php echo $row["user"]; ?></td>
                <td><?php echo $row["topicid"]; ?></td>
                <td><?php echo $row["text"]; ?></td>
                <td><?php echo $row["date"]; ?></td>
            </tr>
            <?php
            $i++;
        }
        ?>
        </tbody>
    </table>


</div>

</body>

</html>
<?php
global $conn;
session_start();
include 'database.php';


if (!isset($_SESSION['user'])) {
    // Redirect the user to another page or display an error message
    header("Location: index.php"); // Replace "login.php" with the appropriate page
    exit(); // Terminate the script to prevent further execution
}

// Pagination variables
$rowsPerPage = 5; // Number of rows to display per page
$currentpage = isset($_GET['page']) ? $_GET['page'] : 1; // Current page number, default is 1

$id = $_SESSION['user']['id'];
$offset = ($currentpage - 1) * $rowsPerPage; // Calculate the offset for the SQL query

// Query to retrieve rows with pagination
$result = mysqli_query($conn, "SELECT * FROM Files WHERE userid = $id LIMIT $offset, $rowsPerPage");


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
    <table>
        <thead>
        <tr>
            <th>ID</th>
            <th>User id</th>
            <th>Filename</th>
            <th>Filepath</th>
            <th>Size</th>
        </tr>
        </thead>
        <tbody>
        <?php
        $i = $offset + 1; // Start index for the displayed rows
        while ($row = mysqli_fetch_array($result)) {
            ?>
            <tr id="<?php echo $row["id"]; ?>">
                <td><?php echo $i; ?></td>
                <td><?php echo $row["userid"]; ?></td>
                <td><?php echo $row["filename"]; ?></td>
                <td><?php echo $row["filepath"]; ?></td>
                <td><?php echo $row["size"]; ?></td>
            </tr>
            <?php
            $i++;
        }
        ?>
        </tbody>
    </table>
    <!-- Pagination links -->
    <?php
    // Query to get the total number of rows
    $countResult = mysqli_query($conn, "SELECT COUNT(*) as total FROM Files WHERE userid = $id");
    $countRow = mysqli_fetch_assoc($countResult);
    $totalRows = $countRow['total'];

    // Calculate the total number of pages
    $totalPages = ceil($totalRows / $rowsPerPage);

    // Generate pagination links
    echo '<div class="pagination">';
    for ($page = 1; $page <= $totalPages; $page++) {
        echo '<a href="main-page.php?page=' . $page . '">' . $page . '</a>&nbsp;&nbsp;&nbsp;';
    }
    echo '</div>';
    ?>


</div>

</body>

</html>

<script>
    // Get all filenames from the file listing table
    var filenames = [];
    var fileRows = document.querySelectorAll('tbody tr');
    fileRows.forEach(function (row) {
        var filename = row.querySelector('td:nth-child(3)').textContent;
        filenames.push(filename);
    });

    // Compute the most popular file
    var counts = {};
    var maxCount = 0;
    var popularFile = '';
    filenames.forEach(function (filename) {
        counts[filename] = (counts[filename] || 0) + 1;
        if (counts[filename] > maxCount) {
            maxCount = counts[filename];
            popularFile = filename;
        }
        console.log(filename + " ");
    });

    console.log('Most popular file: ' + popularFile + ' (occurrences: ' + maxCount + ')');
</script>

<?php
include 'database.php';

// Get the selected filter criteria from the AJAX request
//$type = $_POST['type'];
//
//// Construct the SQL query based on the selected filter criteria
//$query = "SELECT * FROM Document";
//if (!empty($type)) {
//    $query .= " WHERE types = '$type'";
//}
//
//// Execute the query
//$result = mysqli_query($conn, $query);

$filter = $_POST['filter'];

$query = "SELECT * FROM Document";

// Add filter condition if a value is provided
if (!empty($filter)) {
    $query .= " WHERE types LIKE '%$filter%' OR format LIKE '%$filter%'";
}

$result = mysqli_query($conn, $query);


// Generate the HTML markup for the filtered documents

$output = '';
$i = 1;

while ($row = mysqli_fetch_array($result)) {
    $output .= '
        <tr id="' . $row["id"] . '">
            <td>
                <span class="custom-checkbox">
                    <input type="checkbox" class="user_checkbox" data-user-id="' . $row["id"] . '">
                    <label for="checkbox2"></label>
                </span>
            </td>
            <td>' . $i . '</td>
            <td>' . $row["author"] . '</td>
            <td>' . $row["title"] . '</td>
            <td>' . $row["pages"] . '</td>
            <td>' . $row["types"] . '</td>
            <td>' . $row["format"] . '</td>
            <td>
                <a href="#editDocumentModal" class="edit" data-toggle="modal">
                    <i class="material-icons update" data-toggle="tooltip"
                        data-id="' . $row["id"] . '"
                        data-author="' . $row["author"] . '"
                        data-title="' . $row["title"] . '"
                        data-pages="' . $row["pages"] . '"
                        data-types="' . $row["types"] . '"
                        data-format="' . $row["format"] . '"
                        title="Edit"></i>
                </a>
                <a href="#deleteDocumentModal" class="delete" data-id="' . $row["id"] . '" data-toggle="modal">
                    <i class="material-icons" data-toggle="tooltip" title="Delete"></i>
                </a>
            </td>
        </tr>';

    $i++;
}

echo $output;
?>

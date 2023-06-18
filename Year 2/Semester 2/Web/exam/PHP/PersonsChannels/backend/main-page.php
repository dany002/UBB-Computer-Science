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

    <script>
        $(document).ready(function() {
            $.ajax({
                data: {
                    type: 3,
                },
                type: "POST",
                url: "save.php",
                success: function (dataResult) {
                    var channels = JSON.parse(dataResult);
                    populateSubscribeChannelTable(channels);
                }
            });
        });


        function populateSubscribeChannelTable(channels){
            var tableBody = document.getElementById("channel-subscribed-table-body");
            tableBody.innerHTML = "";

            for (var i = 0; i < channels.length; i++) {
                var channel = channels[i];
                var row = document.createElement("tr");
                row.id = channel.id;

                var indexCell = document.createElement("td");
                indexCell.textContent = i + 1;
                row.appendChild(indexCell);


                var nameCell = document.createElement("td");
                nameCell.textContent = channel.name;
                row.appendChild(nameCell);

                var descriptionCell = document.createElement("td");
                descriptionCell.textContent = channel.description;
                row.appendChild(descriptionCell);


                var actionCell = document.createElement("td");
                var subscribeButton = document.createElement("button");
                subscribeButton.type = "button";
                subscribeButton.textContent = "Unsubscribe";
                actionCell.appendChild(subscribeButton);
                row.appendChild(actionCell);

                tableBody.appendChild(row);
            }
        }

    </script>

    <style>
        .login {
            font-size: 40px;

        }


        .container {
            justify-content: center;
            align-items: flex-start;
            margin-top: 50px;
        }

        .filter,
        .subscribed {
            margin: 0 20px;
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
    <div class="filter">
        <h3>Check the channels owned by a specific person</h3>
        <input id="find-channel-input" type="text" placeholder="Owner">
        <button id="find-channel-btn" type="submit">Check</button>

        <table>
            <thead>
            <tr>
                <th>ID</th>
                <th>Owner</th>
                <th>Name</th>
                <th>Description</th>
                <th>Subscribers</th>
                <th>Action</th>
            </tr>
            </thead>
            <tbody id="channel-table-body"></tbody>
        </table>

    </div>
    <div class="subscribed">
        <h3>These are the channels that you are subscribed</h3>
        <table>
            <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Description</th>
                <th>Action</th>
            </tr>
            </thead>

            <tbody id="channel-subscribed-table-body"></tbody>
        </table>
    </div>
</div>

</body>

</html>


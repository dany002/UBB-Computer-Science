<?php
global $conn;
include 'database.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Plans</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="ajax.js"></script>
    <script>
        $(document).ready(function() {
            $.ajax({
                data: {
                    type: 1,
                },
                type: "POST",
                url: "save.php",
                success: function (dataResult) {
                    console.log(dataResult);
                    var cities = JSON.parse(dataResult);
                    populateCitiesTable(cities);
                }
            });
        });


        function populateCitiesTable(cities){
            var tableBody = document.getElementById("cities-table-body");
            tableBody.innerHTML = "";

            for (var i = 0; i < cities.length; i++) {
                var city = cities[i];
                var row = document.createElement("tr");
                row.id = city.id;

                var indexCell = document.createElement("td");
                indexCell.textContent = i + 1;
                row.appendChild(indexCell);


                // var nameCell = document.createElement("td");
                // nameCell.textContent = city.name;
                // row.appendChild(nameCell);

                var nameCell = document.createElement("td");
                var nameLink = document.createElement("a");
                nameLink.href = "main-page.php?id=" + city.id;
                nameLink.textContent = city.name;
                nameCell.appendChild(nameLink);
                row.appendChild(nameCell);

                var countyCell = document.createElement("td");
                countyCell.textContent = city.county;
                row.appendChild(countyCell);



                // var actionCell = document.createElement("td");
                // var subscribeButton = document.createElement("button");
                // subscribeButton.type = "button";
                // subscribeButton.textContent = "Unsubscribe";
                // actionCell.appendChild(subscribeButton);
                // row.appendChild(actionCell);

                tableBody.appendChild(row);
            }
        }

    </script>




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
            <th>Name</th>
            <th>County</th>
        </tr>
        </thead>
        <tbody id="cities-table-body"></tbody>
    </table>

</div>
</body>

</html>

<?php
global $conn;
include 'database.php';

$currentId = isset($_GET['id']) ? $_GET['id'] : 1; // Current id, default is 1
$prev = isset($_GET['prev']) ? $_GET['prev'] : 1

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

        var route = JSON.parse(localStorage.getItem("route")) || [];


        $(document).ready(function() {



            $.ajax({
                data: {
                    id: <?php echo $currentId; ?>,
                    type: 2,
                },
                type: "POST",
                url: "save.php",
                success: function (dataResult) {
                    //console.log(dataResult);
                    var links = JSON.parse(dataResult);
                    //console.log(links);

                    populateLinksTable(links);


                    route.push(<?php echo $currentId; ?>)

                    localStorage.setItem("route", JSON.stringify(route));
                }
            });
        });


        $(document).on('click', '#go-back-btn', function (e) {
            var route = JSON.parse(localStorage.getItem("route")) || [];

            console.log("HI");
            for (var i = 0; i < route.length; i++) {
                console.log(route[i]);
            }
            if (route.length > 1) {
                route.pop();

                console.log("LENGTH ROUTE AFTER POP" + route.length);
                var prevLinkId = route[route.length - 1];

                localStorage.setItem("route", JSON.stringify(route));

                window.location.href = "main-page.php?id=" + prevLinkId;
            }
        });

        function populateLinksTable(links){
            var tableBody = document.getElementById("links-table-body");
            tableBody.innerHTML = "";


            for (var i = 0; i < links.length; i++) {
                var link = links[i];
                var row = document.createElement("tr");
                row.id = link.id;

                var indexCell = document.createElement("td");
                indexCell.textContent = i + 1;
                row.appendChild(indexCell);


                // var nameCell = document.createElement("td");
                // nameCell.textContent = city.name;
                // row.appendChild(nameCell);

                var firstCityCell = document.createElement("td");
                var firstCityLink = document.createElement("a");
                firstCityLink.href = "main-page.php?id=" + link.idcity1 //+ "&prev=" + <?php echo $currentId; ?>;
                firstCityLink.textContent = link.city1_name;
                firstCityCell.appendChild(firstCityLink);
                row.append(firstCityCell);



                var secondCityCell = document.createElement("td");
                var secondCityLink = document.createElement("a");
                secondCityLink.href = "main-page.php?id=" + link.idcity2 //+ "&prev=" + <?php echo $currentId; ?>;
                secondCityLink.textContent = link.city2_name;
                secondCityCell.appendChild(secondCityLink);
                row.append(secondCityCell);

                var durationCell = document.createElement("td");
                durationCell.textContent = link.duration;
                row.append(durationCell);

                var distanceCell = document.createElement("td");
                distanceCell.textContent = link.distance;
                row.append(distanceCell);


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
            <th>Departure</th>
            <th>Destination</th>
            <th>Duration</th>
            <th>Distance</th>
        </tr>
        </thead>
        <tbody id="links-table-body"></tbody>
    </table>
    <button id="go-back-btn" type="button">Go back</button>

</div>
</body>

</html>

$(document).on('click', '#login_btn', function (e){
    var username = $('#login_user').val();
    if(username.length === 0) {
        alert("Please insert a username");
        return 0;
    }

    $.ajax({
        data: {
            type: 1,
            username: username
        },
        type: "POST",
        url: "save.php",
        success: function (dataResult){
            var dataResult = JSON.parse(dataResult);
            console.log(dataResult)
            if(dataResult.statusCode===200){
                alert("Hi there");
                // go to main page
                window.location.href = 'main-page.php'
            }
            else{
                alert("Authentication failed!");
            }
        }
    });
});

$(document).on('click', '#find-channel-btn', function (e) {
    var owner = $('#find-channel-input').val();
    $.ajax({
        data: {
            type: 2,
            owner: owner
        },
        type: "POST",
        url: "save.php",
        success: function (dataResult) {
            var channels = JSON.parse(dataResult);
            channels["owner"] = owner;
            populateChannelTable(channels);
        }
    });
});

function populateChannelTable(channels) {
    var tableBody = document.getElementById("channel-table-body");
    tableBody.innerHTML = ""; // Clear existing rows

    for (var i = 0; i < channels.length; i++) {
        var channel = channels[i];
        var row = document.createElement("tr");
        row.id = channel.id;

        var indexCell = document.createElement("td");
        indexCell.textContent = i + 1;
        row.appendChild(indexCell);

        var ownerIdCell = document.createElement("td");
        ownerIdCell.textContent = channels.owner;
        row.appendChild(ownerIdCell);

        var nameCell = document.createElement("td");
        nameCell.textContent = channel.name;
        row.appendChild(nameCell);

        var descriptionCell = document.createElement("td");
        descriptionCell.textContent = channel.description;
        row.appendChild(descriptionCell);

        var subscribersCell = document.createElement("td");
        subscribersCell.textContent = channel.subscribers;
        row.appendChild(subscribersCell);

        var actionCell = document.createElement("td");
        var subscribeButton = document.createElement("button");
        subscribeButton.id = "subscribe-button";
        subscribeButton.type = "button";
        subscribeButton.textContent = "Subscribe";
        actionCell.appendChild(subscribeButton);
        row.appendChild(actionCell);

        tableBody.appendChild(row);
    }
}

$(document).on('click', '#subscribe-button', function (e){
    console.log("HEYA")
    $.ajax({
        data: {
            type: 4,
        },
        type: "POST",
        url: "save.php",
        success: function (dataResult) {
            var row = JSON.parse(dataResult);
            console.log("IT worked");
            console.log(row);
        }
    });
})

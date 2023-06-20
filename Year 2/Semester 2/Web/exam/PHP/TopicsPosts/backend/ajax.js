$(document).on('click', '#login_btn', function (e){
    var username = $('#login_user').val();
    if(username.length === 0) {
        alert("Please insert a username");
        return 0;
    }

    $.ajax({
        data: {
            type: 1,
            username: username,
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

$(document).on('click','#topic_name_btn', function (e){
    var topic_name = $('#topic_name_input').val();
    if(topic_name.length === 0){
        alert("Please add the topic name");
        return 0;
    }

    var text = $('#post_text_input').val();
    if(text.length === 0){
        alert("Please add some text for the new post");
        return 0;
    }

    $.ajax({
        data: {
            type: 2,
            topic: topic_name,
            text: text,
        },
        type: "POST",
        url: "save.php",
        success: function(dataResult){
            console.log(dataResult)
            var dataResult = JSON.parse(dataResult);
            console.log(this.data);
            refreshTable();
        }
    })
})




$(document).on('click', '.update-btn', function() {
    var postId = $(this).data('id');
    var newText = $('#update-text-input').val();

    if (newText.length === 0) {
        alert("Text is empty!");
        return 0;
    }

    $.ajax({
        data: {
            type: 3,
            id: postId,
            text: newText,
        },
        type: 'POST',
        url: 'save.php',
        success: function (response) {
            console.log(response);
            refreshTable();
        }
    });
});




function refreshTable() {
    $.ajax({
        url: 'fetch-posts.php',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            $('#post-table-body').empty();

            $.each(data, function(index, row) {
                $('#post-table-body').append(`
                    <tr id="${row.id}">
                        <td>${index+1}</td>
                        <td>${row.user}</td>
                        <td>${row.topic}</td>
                        <td>${row.text}</td>
                        <td>${row.date}</td>
                        <td>
                          <button class="update-btn" data-id="${row.id}">Update</button>
                        </td>
                    </tr>
        `       );
            });
        }
    });
}

refreshTable();













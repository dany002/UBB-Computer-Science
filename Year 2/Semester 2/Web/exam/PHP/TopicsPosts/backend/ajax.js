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
        }
    })
})

















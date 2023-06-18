$(document).on('click', '#register_btn', function (e){
    var username = $('#register_user').val();
    if(username.length === 0) {
        alert("Please insert a username");
        return 0;
    }

    var password = $('#register_password').val();
    if(password.length === 0){
        alert("Please insert a password");
        return 0;
    }


    $.ajax({
        data: {
            type: 1,
            username: username,
            password: password
        },
        type: "POST",
        url: "save.php",
        success: function (dataResult){
            var dataResult = JSON.parse(dataResult);
            if(dataResult.statusCode===200){
                alert("Register worked! Now you have to login");
            }
            else{
                alert("Register failed!");
            }
        }
    });
});


$(document).on('click', '#login_btn', function (e){
    var username = $('#login_user').val();
    if(username.length === 0) {
        alert("Please insert a username");
        return 0;
    }

    var password = $('#login_password').val();
    if(password.length === 0){
        alert("Please insert a password");
        return 0;
    }


    $.ajax({
        data: {
            type: 2,
            username: username,
            password: password
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
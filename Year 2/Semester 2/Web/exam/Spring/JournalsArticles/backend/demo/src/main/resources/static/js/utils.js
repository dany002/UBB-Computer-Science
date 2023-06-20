


//function deleteStudent(id) {
//    console.log("Calling Ajax delete..");
//    $.ajax({
//        url: 'student/delete',
//        type: 'DELETE',
//        data: {id: id},
//        success: function (data, status) {
//        }
//    });
//}
//
//function updateStudent() {
//    console.log("Calling Ajax update..");
//    let data = {'id': $("#idUpdate").val(), 'nume': $("#numeUpdate").val(),
//        'specializare': $("#specializareUpdate").val(), 'grupa': $("#grupaUpdate").val()};
//    console.log('data=', data);
//    $.ajax({
//        url: 'student/update',
//        type: 'PUT',
//        contentType: 'application/json',
//        data: JSON.stringify(data),
//        processData: false,
//        success: function (data, status) {
//        }
//    });
//}
//
//$(document).ready(function(){
//    $("#deletebtn").click(function() {
//        deleteStudent($("#iddelete").val());
//    });
//
//    $("#updatebtn").click(function() {
//        updateStudent();
//    });
//});


$(document).on('click', '#login_btn', function (e){
    var username = $('#login_user').val();
    if(username.length === 0) {
        alert("Please insert a username");
        return 0;
    }
    let data = {'username': username};

    $.ajax({
        url: '/login',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        processData: false,
        success: function (dataResult){
            window.location.href = 'main-page.html'
        }
    });
});


$(document).on('click', '#get_articles_btn', function(e){
    var journal = $('#journal_input').val();
    if(journal.length === 0){
        alert("Please insert a journal");
        return 0;
    }

    var url = '/articles/all?journalName=' + encodeURIComponent(journal);


    $.ajax({
        url: url,
        type: 'GET',
        contentType: 'application/json',
        success: function(dataResult) {
            console.log(dataResult);
            populateArticlesForASpecificJournalTable(dataResult);
        }
    });
})

function populateArticlesForASpecificJournalTable(articles){
    var tableBody = document.getElementById("articles-for-a-specific-journal-table");
    tableBody.innerHTML = "";

    for (var i = 0; i < articles.length; i++) {
        var article = articles[i];
        var row = document.createElement("tr");
        row.id = article.id;

        var indexCell = document.createElement("td");
        indexCell.textContent = i + 1;
        row.appendChild(indexCell);


        var summaryCell = document.createElement("td");
        summaryCell.textContent = article.summary;
        row.appendChild(summaryCell);

        var dateCell = document.createElement("td");
        dateCell.textContent = article.date;
        row.appendChild(dateCell);

        tableBody.appendChild(row);
    }
}

$(document).on('click', '#add_article_btn', function (e){
    var journalName = $('#journal_input_add_article').val();
    if(journalName.length === 0) {
        alert("Please insert a journal");
        return 0;
    }

    var summary = $('#summary_input_add_article').val();
    if(summary.length === 0){
        alert("Plase insert a summary");
        return 0;
    }
    let data = {'journalname': journalName, 'summary': summary};

    $.ajax({
        url: '/articles/add',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        processData: false,
        success: function (dataResult){
            console.log(dataResult);
            console.log("IT worked");
        }
    });
});
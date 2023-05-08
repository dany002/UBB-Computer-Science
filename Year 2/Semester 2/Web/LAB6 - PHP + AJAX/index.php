<?php
include 'database.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Documents Data</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="ajax.js"></script>
</head>
<body>

<div class="container">
    <p id="success"></p>
    <div class="table-wrapper">
        <div class="table-title">
            <div class="row">
                <div class="col-sm-6">
                    <h2>Manage <b>Documents</b></h2>
                </div>
                <div class="col-sm-6">
                    <a href="#addDocumentModal" class="btn btn-success" data-toggle="modal"><i class="material-icons"></i> <span>Add New Document</span></a>
                    <a href="JavaScript:void(0);" class="btn btn-danger" id="delete_multiple"><i class="material-icons"></i> <span>Delete</span></a>
                </div>
            </div>
        </div>
        <div class="col-sm-2">
            <input type="text" id="filter" name="filter" class="form-control" placeholder="Filter by type or format">

            <!--            <label for="typeFilter">Type:</label>-->
<!--            <select id="typeFilter" class="form-control">-->
<!--                <option value="">All</option>-->
<!--                <option value="wddsa">dsa</option>-->
<!--                <option value="Document Type 2">Document Type 2</option>-->
<!--                Add more options based on your document types  -->
<!--            </select>-->
        </div>
        <table class="table table-striped table-hover">
            <thead>
            <tr>
                <th>
						<span class="custom-checkbox">
							<input type="checkbox" id="selectAll">
							<label for="selectAll"></label>
						</span>
                </th>
                <th>SL NO</th>
                <th>AUTHOR</th>
                <th>TITLE</th>
                <th>PAGES</th>
                <th>TYPES</th>
                <th>FORMAT</th>
                <th>ACTION</th>
            </tr>
            </thead>
            <tbody>

            <?php
            $result = mysqli_query($conn,"SELECT * FROM Document");
            $i=1;
            while($row = mysqli_fetch_array($result)) {
                ?>
                <tr id="<?php echo $row["id"]; ?>">
                    <td>
						<span class="custom-checkbox">
							<input type="checkbox" class="user_checkbox" data-user-id="<?php echo $row["id"]; ?>">
							<label for="checkbox2"></label>
						</span>
                    </td>
                    <td><?php echo $i; ?></td>
                    <td><?php echo $row["author"]; ?></td>
                    <td><?php echo $row["title"]; ?></td>
                    <td><?php echo $row["pages"]; ?></td>
                    <td><?php echo $row["types"]; ?></td>
                    <td><?php echo $row["format"]; ?></td>
                    <td>
                        <a href="#editDocumentModal" class="edit" data-toggle="modal">
                            <i class="material-icons update" data-toggle="tooltip"
                               data-id="<?php echo $row["id"]; ?>"
                               data-author="<?php echo $row["author"]; ?>"
                               data-title="<?php echo $row["title"]; ?>"
                               data-pages="<?php echo $row["pages"]; ?>"
                               data-types="<?php echo $row["types"]; ?>"
                               data-format="<?php echo $row["format"]; ?>"
                               title="Edit"></i>
                        </a>
                        <a href="#deleteDocumentModal" class="delete" data-id="<?php echo $row["id"]; ?>" data-toggle="modal"><i class="material-icons" data-toggle="tooltip"
                                                                                                                                 title="Delete"></i></a>
                    </td>
                </tr>
                <?php
                $i++;
            }
            ?>
            </tbody>
        </table>

    </div>
</div>
<!-- Add Modal HTML -->
<div id="addDocumentModal" class="modal fade">
    <div class="modal-dialog">
        <div class="modal-content">
            <form id="user_form" onsubmit="return validateForm('user_form');">
                <div class="modal-header">
                    <h4 class="modal-title">Add Document</h4>
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                </div>
                <div class="modal-body">
                    <div class="form-group">
                        <label>Author</label>
                        <input type="text" id="author" name="author" class="form-control" pattern=".*\S.*" required>
                    </div>
                    <div class="form-group">
                        <label>Title</label>
                        <input type="text" id="title" name="title" class="form-control" pattern=".*\S.*" required>
                    </div>
                    <div class="form-group">
                        <label>Pages</label>
                        <input type="text" id="pages" name="pages" class="form-control" pattern="\d+" required>
                    </div>
                    <div class="form-group">
                        <label>Types</label>
                        <input type="text" id="types" name="types" class="form-control" pattern=".*\S.*" required>
                    </div>
                    <div class="form-group">
                        <label>Format</label>
                        <input type="text" id="format" name="format" class="form-control" pattern=".*\S.*" required>
                    </div>
                </div>
                <div class="modal-footer">
                    <input type="hidden" value="1" name="type">
                    <input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
                    <button type="button" class="btn btn-success" id="btn-add">Add</button>
                </div>
            </form>
        </div>
    </div>
</div>
<!-- Edit Modal HTML -->
<div id="editDocumentModal" class="modal fade">
    <div class="modal-dialog">
        <div class="modal-content">
            <form id="update_form" onsubmit="return validateForm('update_form');">
                <div class="modal-header">
                    <h4 class="modal-title">Edit User</h4>
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                </div>
                <div class="modal-body">
                    <input type="hidden" id="id_u" name="id" class="form-control" required>
                    <div class="form-group">
                        <label>Author</label>
                        <input type="text" id="author_u" name="author" class="form-control" pattern=".*\S.*" required>
                    </div>
                    <div class="form-group">
                        <label>Title</label>
                        <input type="text" id="title_u" name="title" class="form-control" pattern=".*\S.*" required>
                    </div>
                    <div class="form-group">
                        <label>Pages</label>
                        <input type="text" id="pages_u" name="pages" class="form-control" pattern="\d+" required>
                    </div>
                    <div class="form-group">
                        <label>Types</label>
                        <input type="text" id="types_u" name="types" class="form-control" pattern=".*\S.*" required>
                    </div>
                    <div class="form-group">
                        <label>Format</label>
                        <input type="text" id="format_u" name="format" class="form-control" pattern=".*\S.*" required>
                    </div>
                </div>
                <div class="modal-footer">
                    <input type="hidden" value="2" name="type">
                    <input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
                    <button type="button" class="btn btn-info" id="update">Update</button>
                </div>
            </form>
        </div>
    </div>
</div>
<!-- Delete Modal HTML -->
<div id="deleteDocumentModal" class="modal fade">
    <div class="modal-dialog">
        <div class="modal-content">
            <form>
                <div class="modal-header">
                    <h4 class="modal-title">Delete Document</h4>
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                </div>
                <div class="modal-body">
                    <input type="hidden" id="id_d" name="id" class="form-control">
                    <p>Are you sure you want to delete these Records?</p>
                    <p class="text-warning"><small>This action cannot be undone.</small></p>
                </div>
                <div class="modal-footer">
                    <input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
                    <button type="button" class="btn btn-danger" id="delete">Delete</button>
                </div>
            </form>
        </div>
    </div>
</div>

</body>
</html>
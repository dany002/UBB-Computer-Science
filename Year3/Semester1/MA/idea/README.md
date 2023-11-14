Jira app

-> open the app
	-> first page - "get tasks"
		-> will contain a list with all the tasks
		-> a button "+" in order to add a new task which will take you to second page (add page)
		-> each task will also have a button that will look like a pen in order to update it (update page) or a trash in order to delete the task.
		-> if you want to delete a task, you will have to put the name of the task in order to confirm that you really want to delete it
	-> second page - "add task"
		-> there you will be able to add a new task by completing the following entries: title, description, deadline, priority, status
		-> after you complete all the entries, it will validate the input to make sure that everything is right and if it is correct, it will send you back to the first page and it will say that the task was successfully created.
		-> if it fails, it will show to you a friendly error, in order to make it work
		-> also on this page there will be 2 buttons on bottom, one with a "Cancel" and one with "Add", "Cancel" means that you do not want to add a task anymore and you will be redirected to first page, "Add" means that you want to add the task.
	-> update page - "update task"
		-> you will be able to update the description, deadline, priority and status, you can't change the title of the task.
		-> there will be validations again and also if everything is alright it will send you back to the first page.
		-> also on this page there will be 2 buttons on bottom, one with a "Update" and one with a "Cancel", "Cancel" means that you do not want to modify that task, so you will be redirected to first page, "Update" means that you want to save the updated task.

In the case of offline usage of the application:
	The user will still be able to retrieve the list of books they own (directly from the local database)
	However, in case of them trying to add a new task, remove or update an already existing one,
	they will get a pop up window with a warning, telling them there is no internet connection
	( therefore the changes cannot be made or saved )
      
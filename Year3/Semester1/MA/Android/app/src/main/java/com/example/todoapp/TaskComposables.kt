package com.example.todoapp
import android.annotation.SuppressLint
import android.widget.CalendarView
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.ArrowDropDown
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.Edit
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.material3.*
import androidx.compose.ui.Alignment
import androidx.navigation.NavController



@Composable
fun TaskList(tasks: List<Task>, onEditClick: (Task) -> Unit, onAddTaskClick: () -> Unit, onDeleteClick: (Task) -> Unit) {
    Column(
        modifier = Modifier.fillMaxSize()
    ) {
        // Add a button with an icon to navigate to the "Add Task" screen
        Button(
            onClick = { onAddTaskClick() },
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
        ) {
            Row(
                verticalAlignment = Alignment.CenterVertically
            ) {
                Icon(imageVector = Icons.Default.Add, contentDescription = "Add Task")
                Spacer(modifier = Modifier.width(8.dp))
                Text("Add Task")
            }
        }

        LazyColumn {
            items(tasks) { task ->
                TaskItem(task = task, onEditClick = onEditClick, onDeleteClick = onDeleteClick)
            }
        }
    }
}

@Composable
fun TaskItem(task: Task, onEditClick: (Task) -> Unit, onDeleteClick: (Task) -> Unit) {
    // Here we set the UI for everything that involves a task (fields) + pen + trash
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(8.dp)
    ) {
        Column(
            modifier = Modifier.padding(16.dp)
        ) {
            Text(text = "Name: ${task.name}")
            Text(text = "Description: ${task.description}")
            Text(text = "Deadline: ${task.deadline}")
            Text(text = "Priority: ${task.priority}")
            Text(text = "Status: ${task.status.name}")
        }
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.End
        ) {
            IconButton(onClick = { onEditClick(task) }) {
                Icon(imageVector = Icons.Default.Edit, contentDescription = "Edit")
            }
            IconButton(onClick = { onDeleteClick(task) }) {
                Icon(imageVector = Icons.Default.Delete, contentDescription = "Delete")
            }
        }
    }
}

@Composable
fun EditTaskScreen(navController: NavController, task: Task, onEditTask: (Task) -> Unit) {
    var editedTask by remember { mutableStateOf(task) }

    val statusOptions = TaskStatus.values().map { it.name }
    var isDropdownExpanded by remember { mutableStateOf(false) }
    var selectedStatus by remember { mutableStateOf(editedTask.status.name) }
    var showErrorDialog by remember { mutableStateOf(false) }
    fun showErrorAlert() {
        showErrorDialog = true
    }


    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text("Edit Task", style = MaterialTheme.typography.headlineSmall)

        // Input fields for editing task details
        TextField(
            value = editedTask.name,
            onValueChange = { editedTask = editedTask.copy(name = it) },
            label = { Text("Name") }
        )

        TextField(
            value = editedTask.description,
            onValueChange = { editedTask = editedTask.copy(description = it) },
            label = { Text("Description") }
        )

        TextField(
            value = editedTask.deadline,
            onValueChange = { editedTask = editedTask.copy(deadline = it) },
            label = { Text("Deadline") }
        )

        TextField(
            value = editedTask.priority,
            onValueChange = { editedTask = editedTask.copy(priority = it) },
            label = { Text("Priority") }
        )

        // Dropdown for selecting TaskStatus
        Row(
            modifier = Modifier.clickable { isDropdownExpanded = true },
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text("Status: $selectedStatus", modifier = Modifier.weight(1f))
            Icon(imageVector = Icons.Default.ArrowDropDown, contentDescription = "Open Dropdown")
        }

        if (isDropdownExpanded) {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .absoluteOffset(
                        x = 0.dp,
                        y = 20.dp
                    )
            ) {
                DropdownMenu(
                    expanded = isDropdownExpanded,
                    onDismissRequest = { isDropdownExpanded = false },
                    modifier = Modifier.fillMaxWidth(),
                ) {
                    statusOptions.forEach { status ->
                        DropdownMenuItem(text = { Text(text = status) }, onClick = {
                            selectedStatus = status
                            isDropdownExpanded = false
                            editedTask = editedTask.copy(status = TaskStatus.valueOf(status))
                        })
                    }
                }
            }
        }

        Spacer(modifier = Modifier.height(16.dp))

        Row() {
            // "Save" button to update the task
            Button(
                onClick = {
                    if (validateFieldsBeforeNavigate(editedTask)) {
                        onEditTask(editedTask)
                        navController.popBackStack() // Navigate back to the previous screen (task list)
                    } else {
                        showErrorAlert()
                    }
                }
            ) {
                Text("Update")
            }
            Button(
                onClick = {
                    navController.popBackStack()
                }
            ) {
                Text("Cancel")
            }
        }
    }
}


@Composable
fun AddTaskScreen(navController: NavController, onAddTask: (Task) -> Unit) {
    var newTask by remember { mutableStateOf(Task("", "", "", "", TaskStatus.TODO)) }

    val statusOptions = TaskStatus.values().map { it.name }
    var isDropdownExpanded by remember { mutableStateOf(false) }
    var selectedStatus by remember { mutableStateOf(newTask.status.name) }
    var showErrorDialog by remember { mutableStateOf(false) }
    fun showErrorAlert() {
        showErrorDialog = true
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text("Add New Task", style = MaterialTheme.typography.headlineSmall)

        // Input fields for adding a new task
        TextField(
            value = newTask.name,
            onValueChange = { newTask = newTask.copy(name = it) },
            label = { Text("Name") }
        )

        TextField(
            value = newTask.description,
            onValueChange = { newTask = newTask.copy(description = it) },
            label = { Text("Description") }
        )

        TextField(
            value = newTask.deadline,
            onValueChange = { newTask = newTask.copy(deadline = it) },
            label = { Text("Deadline") }
        )

        TextField(
            value = newTask.priority,
            onValueChange = { newTask = newTask.copy(priority = it) },
            label = { Text("Priority") }
        )


        // Dropdown for selecting TaskStatus
        Row(
            modifier = Modifier.clickable { isDropdownExpanded = true },
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text("Status: $selectedStatus", modifier = Modifier.weight(1f))
            Icon(imageVector = Icons.Default.ArrowDropDown, contentDescription = "Open Dropdown")
        }

        if (isDropdownExpanded) {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .absoluteOffset(
                        x = 0.dp,
                        y = 20.dp
                    )
            ) {
                DropdownMenu(
                    expanded = isDropdownExpanded,
                    onDismissRequest = { isDropdownExpanded = false },
                    modifier = Modifier.fillMaxWidth()
                ) {
                    statusOptions.forEach { status ->
                        DropdownMenuItem(text = { Text(text = status) }, onClick = {
                            selectedStatus = status
                            isDropdownExpanded = false
                            newTask = newTask.copy(status = TaskStatus.valueOf(status))
                        })
                    }
                }
            }
        }

        Spacer(modifier = Modifier.height(16.dp))

        Row(){
            // "Save" button to add the new task
            Button(
                onClick = {
                    if (validateFieldsBeforeNavigate(newTask)) {
                        onAddTask(newTask)
                        navController.popBackStack() // Navigate back to the previous screen (task list)
                    } else {
                        showErrorAlert()
                    }
                }
            ) {
                Text("Add")
            }
            // "Save" button to add the new task
            Button(
                onClick = {
                    navController.popBackStack()
                }
            ) {
                Text("Cancel")
            }
        }


        if (showErrorDialog) {
            AlertDialog(
                onDismissRequest = { showErrorDialog = false },
                title = { Text("Error") },
                text = { Text("Please fill in all fields.") },
                confirmButton = {
                    Button(
                        onClick = { showErrorDialog = false }
                    ) {
                        Text("OK")
                    }
                }
            )
        }

    }
}

@Composable
fun DeleteTaskScreen(
    navController: NavController,
    task: Task,
    onDeleteTask: (Task) -> Unit
) {
    var enteredTaskName by remember { mutableStateOf("") }
    var showErrorDialog by remember { mutableStateOf(false) }
    fun showErrorAlert() {
        showErrorDialog = true
    }
    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("Delete Task", style = MaterialTheme.typography.headlineSmall)

        Text("Type the following text to delete the task: ${task.name}")

        Spacer(modifier = Modifier.height(16.dp))

        TextField(
            value = enteredTaskName,
            onValueChange = { enteredTaskName = it },
            label = { Text("Confirmation Text") },
            modifier = Modifier.padding(16.dp)
        )

        Spacer(modifier = Modifier.height(16.dp))
        Row(){

            Button(
                onClick = {
                    if (enteredTaskName == task.name) {
                        onDeleteTask(task)
                        navController.popBackStack() // Navigate back to the previous screen (task list)
                    }
                    else {
                        showErrorAlert()
                    }
                },
                modifier = Modifier.padding(16.dp)
            ) {
                Text("Delete")
            }
            Button(
                onClick = {
                    navController.popBackStack() // Navigate back to the previous screen (task list)
                },
                modifier = Modifier.padding(16.dp)
            ) {
                Text("Cancel")
            }
        }

        if (showErrorDialog) {
            AlertDialog(
                onDismissRequest = { showErrorDialog = false },
                title = { Text("Error") },
                text = { Text("The title of task is not the same!") },
                confirmButton = {
                    Button(
                        onClick = { showErrorDialog = false }
                    ) {
                        Text("OK")
                    }
                }
            )
        }
    }
}







fun validateFieldsBeforeNavigate(task: Task): Boolean {
    if(task.name.isEmpty() || task.deadline.isEmpty() || task.description.isEmpty() || task.priority.isEmpty()) // Don't have to validate status
        return false
    return true
}



package com.example.todoapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.runtime.remember
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.Modifier
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.todoapp.ui.theme.ToDoAppTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ToDoAppTheme {
                val tasks = remember { generateSampleTasks() }.toMutableList()
                val navController = rememberNavController()

                NavHost(navController, startDestination = "taskList") {
                    composable("taskList") {
                        TaskList(tasks = tasks, onEditClick = { taskToEdit ->
                            // Navigate to the EditTaskScreen
                            navController.navigate("editTask/${taskToEdit.name}")
                        },
                            onAddTaskClick = {
                                navController.navigate("addTask")
                            },
                            onDeleteClick = { taskToDelete ->
                                navController.navigate("deleteTask/${taskToDelete.name}")
                            })
                    }
                    composable("editTask/{taskName}") { backStackEntry ->
                        val taskName = backStackEntry.arguments?.getString("taskName")
                        val task = tasks.find { it.name == taskName }
                        task?.let {
                            EditTaskScreen(navController, task = it) { editedTask ->
                                val index = tasks.indexOfFirst { it.name == editedTask.name }
                                if (index != -1) {
                                    tasks[index] = editedTask
                                }
                            }
                        }
                    }
                    composable("addTask") {
                        AddTaskScreen(navController, onAddTask = { newTask ->
                            tasks.add(newTask);
                        })
                    }
                    composable("deleteTask/{taskName}") { backStackEntry ->
                        val taskName = backStackEntry.arguments?.getString("taskName")
                        val task = tasks.find { it.name == taskName }
                        task?.let {
                            DeleteTaskScreen(navController, task = it) { taskToDelete ->
                                tasks.remove(taskToDelete)
                            }
                        }
                    }
                }
            }
        }
    }

    private fun generateSampleTasks(): List<Task> {
        return listOf(
            Task("Task 1", "Description 1", "2023-01-01", "High", TaskStatus.IN_PROGRESS),
            Task("Task 2", "Description 2", "2023-02-15", "Medium", TaskStatus.DONE),
            Task("Task 3", "Description 3", "2023-03-31", "Low", TaskStatus.TODO)
        )
    }

}

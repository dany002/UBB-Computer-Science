package com.example.todoapp

data class Task(
    val name: String,
    val description: String,
    val deadline: String,
    val priority: String,
    val status: TaskStatus
)

enum class TaskStatus {
    TODO,
    IN_PROGRESS,
    DONE
}
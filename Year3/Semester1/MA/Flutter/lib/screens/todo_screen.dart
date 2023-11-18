import 'package:flutter/material.dart';
import '../models/task.dart';
import 'task_list.dart';
import 'edit_task_screen.dart';
import 'add_task_screen.dart';
import 'delete_task_screen.dart';

class ToDoScreen extends StatefulWidget {
  @override
  _ToDoScreenState createState() => _ToDoScreenState();
}

class _ToDoScreenState extends State<ToDoScreen> {
  List<Task> tasks = [];

  @override
  void initState() {
    super.initState();
    tasks = generateSampleTasks();
  }

  List<Task> generateSampleTasks() {
    return [
      Task(
        name: "Task 1",
        description: "Description 1",
        deadline: "2023-01-01",
        priority: "High",
        status: TaskStatus.IN_PROGRESS,
      ),
      Task(
        name: "Task 2",
        description: "Description 2",
        deadline: "2023-02-15",
        priority: "Medium",
        status: TaskStatus.DONE,
      ),
      Task(
        name: "Task 3",
        description: "Description 3",
        deadline: "2023-03-31",
        priority: "Low",
        status: TaskStatus.TODO,
      ),
    ];
  }

  void navigateToAddTaskScreen() async {
    final newTask = await Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => AddTaskScreen(
          onAddTask: (Task newTask) {
            setState(() {
              tasks.add(newTask);
            });
          },
        ),
      ),
    );

  }

  void navigateToEditTaskScreen(Task task) async {
    final updatedTask = await Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => EditTaskScreen(
          task: task,
          onUpdateTask: (Task updatedTask) {
            setState(() {
              final index = tasks.indexWhere((t) => t.name == updatedTask.name);
              if (index != -1) {
                tasks[index] = updatedTask;
              }
            });
          },
        ),
      ),
    );
  }

  void navigateToDeleteTaskScreen(Task task) async {
    final isDeleted = await Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => DeleteTaskScreen(
          task: task,
          onDeleteTask: (Task deletedTask) {
            setState(() {
              tasks.remove(deletedTask);
            });
          },
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('To-Do App'),
      ),
      body: TaskList(
        tasks: tasks,
        onEditClick: navigateToEditTaskScreen,
        onAddTaskClick: navigateToAddTaskScreen,
        onDeleteClick: navigateToDeleteTaskScreen,
      ),
    );
  }
}

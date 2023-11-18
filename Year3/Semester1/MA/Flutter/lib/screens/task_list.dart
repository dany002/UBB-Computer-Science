import 'package:flutter/material.dart';
import '../models/task.dart';
import 'edit_task_screen.dart';
import 'add_task_screen.dart';

class TaskList extends StatelessWidget {
  final List<Task> tasks;
  final Function(Task) onEditClick;
  final Function() onAddTaskClick;
  final Function(Task) onDeleteClick;

  TaskList({
    required this.tasks,
    required this.onEditClick,
    required this.onAddTaskClick,
    required this.onDeleteClick,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ElevatedButton(
          onPressed: onAddTaskClick,
          child: const Row(
            children: [
              Icon(Icons.add),
              SizedBox(width: 8),
              Text('Add Task'),
            ],
          ),
        ),
        Expanded(
          child: ListView.builder(
            itemCount: tasks.length,
            itemBuilder: (context, index) {
              return TaskItem(
                task: tasks[index],
                onEditClick: onEditClick,
                onDeleteClick: onDeleteClick,
              );
            },
          ),
        ),
      ],
    );
  }
}

class TaskItem extends StatelessWidget {
  final Task task;
  final Function(Task) onEditClick;
  final Function(Task) onDeleteClick;

  TaskItem({
    required this.task,
    required this.onEditClick,
    required this.onDeleteClick,
  });

  Color getStatusColor(TaskStatus status) {
    switch (status) {
      case TaskStatus.TODO:
        return Colors.red;
      case TaskStatus.IN_PROGRESS:
        return Colors.yellow;
      case TaskStatus.DONE:
        return Colors.green;
      default:
        return Colors.transparent; // Default color
    }
  }

  @override
  Widget build(BuildContext context) {
    String statusText = task.status.toString().split('.').last; // Extracts the enum value without the prefix
    Color backgroundColor = getStatusColor(task.status);

    return Card(
      margin: EdgeInsets.all(8),
      color: backgroundColor, // Set background color based on status
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          ListTile(
            title: Text(
              task.name,
              style: TextStyle(color: Colors.white), // Set text color to white for better visibility
            ),
            subtitle: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  task.description,
                  style: TextStyle(color: Colors.white), // Set text color to white for better visibility
                ),
                SizedBox(height: 4),
                Text(
                  'Deadline: ${task.deadline}',
                  style: TextStyle(color: Colors.white), // Set text color to white for better visibility
                ),
                Text(
                  'Priority: ${task.priority}',
                  style: TextStyle(color: Colors.white), // Set text color to white for better visibility
                ),
                Text(
                  'Status: $statusText',
                  style: TextStyle(color: Colors.white), // Set text color to white for better visibility
                ),
              ],
            ),
            trailing: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                IconButton(
                  icon: Icon(Icons.edit),
                  onPressed: () => onEditClick(task),
                ),
                IconButton(
                  icon: Icon(Icons.delete),
                  onPressed: () => onDeleteClick(task),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

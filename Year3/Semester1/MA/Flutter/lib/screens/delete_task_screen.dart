import 'package:flutter/material.dart';
import '../models/task.dart';

class DeleteTaskScreen extends StatelessWidget {
  final Task task;
  final Function(Task) onDeleteTask;

  DeleteTaskScreen({required this.task, required this.onDeleteTask});

  final TextEditingController taskNameController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Delete Task'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              'Are you sure you want to delete the task "${task.name}"?',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 18),
            ),
            SizedBox(height: 20),
            TextFormField(
              controller: taskNameController,
              decoration: InputDecoration(
                labelText: 'Enter the task name to confirm',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                ElevatedButton(
                  onPressed: () {
                    Navigator.pop(context, false);
                  },
                  child: Text('Cancel'),
                ),
                ElevatedButton(
                  onPressed: () {
                    if (taskNameController.text == task.name) {
                      onDeleteTask(task);
                      Navigator.pop(context, true);
                    } else {
                      showDialog(
                        context: context,
                        builder: (context) {
                          return AlertDialog(
                            title: Text('Incorrect Task Name'),
                            content: Text('Please enter the correct task name to delete.'),
                            actions: [
                              TextButton(
                                onPressed: () {
                                  Navigator.pop(context);
                                },
                                child: Text('OK'),
                              ),
                            ],
                          );
                        },
                      );
                    }
                  },
                  child: Text('Delete Task'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

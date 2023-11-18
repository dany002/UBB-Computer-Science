import 'package:flutter/material.dart';
import '../models/task.dart';

class AddTaskScreen extends StatefulWidget {
  final Function(Task) onAddTask;

  const AddTaskScreen({Key? key, required this.onAddTask}) : super(key: key);

  @override
  _AddTaskScreenState createState() => _AddTaskScreenState();
}

class _AddTaskScreenState extends State<AddTaskScreen> {
  late TextEditingController _nameController;
  late TextEditingController _descriptionController;
  late TextEditingController _deadlineController;
  late TextEditingController _priorityController;
  String _selectedStatus = TaskStatus.TODO.toString(); // Default status

  @override
  void initState() {
    super.initState();
    _nameController = TextEditingController();
    _descriptionController = TextEditingController();
    _deadlineController = TextEditingController();
    _priorityController = TextEditingController();
  }

  @override
  void dispose() {
    _nameController.dispose();
    _descriptionController.dispose();
    _deadlineController.dispose();
    _priorityController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Add Task'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextFormField(
              controller: _nameController,
              decoration: InputDecoration(labelText: 'Name'),
            ),
            TextFormField(
              controller: _descriptionController,
              decoration: InputDecoration(labelText: 'Description'),
            ),
            TextFormField(
              controller: _deadlineController,
              decoration: InputDecoration(labelText: 'Deadline'),
              onTap: () async {
                DateTime? selectedDate = await showDatePicker(
                  context: context,
                  initialDate: DateTime.now(),
                  firstDate: DateTime.now(),
                  lastDate: DateTime(DateTime.now().year + 5),
                );
                if (selectedDate != null) {
                  setState(() {
                    _deadlineController.text = selectedDate.toIso8601String().split('T')[0];
                  });
                }
              },
            ),
            TextFormField(
              controller: _priorityController,
              decoration: InputDecoration(labelText: 'Priority'),
            ),
            SizedBox(height: 20),
            DropdownButtonFormField<String>(
              value: _selectedStatus,
              items: TaskStatus.values.map((status) {
                return DropdownMenuItem<String>(
                  value: status.toString(),
                  child: Text(status.toString().split('.').last),
                );
              }).toList(),
              onChanged: (String? value) {
                if (value != null) {
                  setState(() {
                    _selectedStatus = value;
                  });
                }
              },
              decoration: InputDecoration(labelText: 'Status'),
            ),
            SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton(
                  onPressed: () {
                    final String name = _nameController.text;
                    final String description = _descriptionController.text;
                    final String deadline = _deadlineController.text;
                    final String priority = _priorityController.text;

                    if (name.isNotEmpty &&
                        description.isNotEmpty &&
                        deadline.isNotEmpty &&
                        priority.isNotEmpty) {
                      final Task newTask = Task(
                        name: name,
                        description: description,
                        deadline: deadline,
                        priority: priority,
                        status: TaskStatus.values
                            .firstWhere((status) => status.toString() == _selectedStatus),
                      );

                      widget.onAddTask(newTask);
                      Navigator.pop(context);
                    } else {
                      showDialog(
                        context: context,
                        builder: (BuildContext context) {
                          return AlertDialog(
                            title: const Text('Error'),
                            content: const Text('Please fill in all fields.'),
                            actions: [
                              TextButton(
                                onPressed: () {
                                  Navigator.pop(context);
                                },
                                child: const Text('OK'),
                              ),
                            ],
                          );
                        },
                      );
                    }
                  },
                  child: Text('Add'),
                ),
                ElevatedButton(
                  onPressed: () {
                    Navigator.pop(context);
                  },
                  child: Text('Cancel'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

import 'package:flutter/material.dart';
import '../models/task.dart';
import 'package:intl/intl.dart';


class EditTaskScreen extends StatefulWidget {
  final Task task;
  final Function(Task) onUpdateTask;

  EditTaskScreen({required this.task, required this.onUpdateTask});

  @override
  _EditTaskScreenState createState() => _EditTaskScreenState();
}

class _EditTaskScreenState extends State<EditTaskScreen> {
  late TextEditingController nameController;
  late TextEditingController descriptionController;
  late TextEditingController deadlineController;
  late TextEditingController priorityController;
  final _formKey = GlobalKey<FormState>();
  String _selectedStatus = '';

  @override
  void initState() {
    super.initState();
    nameController = TextEditingController(text: widget.task.name);
    descriptionController = TextEditingController(text: widget.task.description);
    deadlineController = TextEditingController(text: widget.task.deadline);
    priorityController = TextEditingController(text: widget.task.priority);
    _selectedStatus = widget.task.status.toString();
  }

  @override
  void dispose() {
    nameController.dispose();
    descriptionController.dispose();
    deadlineController.dispose();
    priorityController.dispose();
    super.dispose();
  }

  Future<void> _selectDate(BuildContext context) async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate: DateTime.now(),
      firstDate: DateTime(2000),
      lastDate: DateTime(2101),
    );

    if (picked != null) {
      setState(() {
        final formattedDate = DateFormat('yyyy-MM-dd').format(picked); // Format the date
        deadlineController.text = formattedDate; // Update the deadline field
      });
    }
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Edit Task'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextFormField(
                controller: nameController,
                decoration: InputDecoration(labelText: 'Name'),
                validator: (value) {
                  if (value!.isEmpty) {
                    return 'Please enter a name';
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: descriptionController,
                decoration: InputDecoration(labelText: 'Description'),
                validator: (value) {
                  if (value!.isEmpty) {
                    return 'Please enter a description';
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: deadlineController,
                decoration: InputDecoration(labelText: 'Deadline'),
                validator: (value) {
                  if (value!.isEmpty) {
                    return 'Please enter a deadline';
                  }
                  return null;
                },
                onTap: () {
                  _selectDate(context); // Open calendar on tap
                },
                readOnly: true,
              ),
              TextFormField(
                controller: priorityController,
                decoration: InputDecoration(labelText: 'Priority'),
                validator: (value) {
                  if (value!.isEmpty) {
                    return 'Please enter a priority';
                  }
                  return null;
                },
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
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  ElevatedButton(
                    onPressed: () {
                      Navigator.pop(context);
                    },
                    child: Text('Cancel'),
                  ),
                  ElevatedButton(
                    onPressed: () {
                      if (_formKey.currentState!.validate()) {
                        Task updatedTask = Task(
                          name: nameController.text,
                          description: descriptionController.text,
                          deadline: deadlineController.text,
                          priority: priorityController.text,
                          status: TaskStatus.values
                              .firstWhere((status) => status.toString() == _selectedStatus),
                        );

                        widget.onUpdateTask(updatedTask);
                        Navigator.pop(context);
                      }
                    },
                    child: Text('Update Task'),
                  )
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

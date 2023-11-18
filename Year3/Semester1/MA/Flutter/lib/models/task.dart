class Task {
  final String name;
  final String description;
  final String deadline;
  final String priority;
  final TaskStatus status;

  Task({
    required this.name,
    required this.description,
    required this.deadline,
    required this.priority,
    required this.status,
  });
}

enum TaskStatus {
  TODO,
  IN_PROGRESS,
  DONE
}

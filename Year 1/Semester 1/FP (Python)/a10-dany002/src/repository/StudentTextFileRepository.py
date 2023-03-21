from repository.StudentRepository import StudentRepository
from domain.Student import Student
import os.path

class StudentTextFileRepository(StudentRepository):
    def __init__(self, file_name):
        super().__init__()

        self._file_name = file_name
        if not os.path.exists(self._file_name):
            self._save_file()
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")
        for line in file.readlines():
            student_id, name = line.split(maxsplit=1, sep=',')
            self.add_a_student(Student(int(student_id), name.rstrip()))
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wt")

        for student in self._students:
            file.write(str(student.student_id) + ',' + student.name + "\n")
        file.close()

    def add_a_student(self, student_that_is_going_to_be_added):
        super(StudentTextFileRepository, self).add_a_student(student_that_is_going_to_be_added)
        self._save_file()

    def remove_a_student(self, student_id):
        super(StudentTextFileRepository, self).remove_a_student(student_id)
        self._save_file()

    def update_a_student_by_id(self, student_id, new_student_name):
        super(StudentTextFileRepository, self).update_a_student_by_id(student_id, new_student_name)
        self._save_file()

    def update_a_student_by_name(self, student_name, new_student_id):
        super(StudentTextFileRepository, self).update_a_student_by_name(student_name, new_student_id)

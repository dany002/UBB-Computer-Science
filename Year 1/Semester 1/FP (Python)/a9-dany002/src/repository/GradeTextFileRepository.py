from repository.GradeRepository import GradeRepository
from domain.Grade import Grade
import os.path

class GradeTextFileRepository(GradeRepository):
    def __init__(self, file_name):
        super().__init__()

        self._file_name = file_name
        if not os.path.exists(self._file_name):
            self._save_file()
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")
        for line in file.readlines():
            student_id, discipline_id, grade_value = line.split(maxsplit=2, sep=',')
            self.add_a_grade_for_a_student(Grade(int(student_id), int(discipline_id), int(grade_value)))
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wt")

        for grade in self._grades:
            file.write(str(grade.student_id) + ',' + str(grade.discipline_id) + ',' + str(grade.grade_value) + "\n")
        file.close()

    def add_a_grade_for_a_student(self, grade_that_is_going_to_be_added):
        super(GradeTextFileRepository, self).add_a_grade_for_a_student(grade_that_is_going_to_be_added)
        self._save_file()

    def remove_grades_for_a_student(self, student_id):
        super(GradeTextFileRepository, self).remove_grades_for_a_student(student_id)
        self._save_file()

    def remove_grades_for_a_discipline(self, discipline_id):
        super(GradeTextFileRepository, self).remove_grades_for_a_discipline(discipline_id)

    def remove_a_grade_for_a_student_at_a_discipline(self, student_id, discipline_id, grade_value):
        super(GradeTextFileRepository, self).remove_a_grade_for_a_student_at_a_discipline(student_id, discipline_id, grade_value)
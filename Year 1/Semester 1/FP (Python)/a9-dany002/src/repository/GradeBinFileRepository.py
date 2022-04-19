from repository.GradeRepository import GradeRepository
import pickle
import os.path

class GradeBinFileRepository(GradeRepository):
    def __init__(self, file_name):
        super().__init__()

        self.__file_name = file_name
        if not os.path.exists(self.__file_name):
            self._save_file()
        self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "rb")
        self._grades = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._grades, file)
        file.close()

    def add_a_grade_for_a_student(self, grade_that_is_going_to_be_added):
        super(GradeBinFileRepository, self).add_a_grade_for_a_student(grade_that_is_going_to_be_added)
        self._save_file()

    def remove_grades_for_a_student(self, student_id):
        super(GradeBinFileRepository, self).remove_grades_for_a_student(student_id)
        self._save_file()

    def remove_grades_for_a_discipline(self, discipline_id):
        super(GradeBinFileRepository, self).remove_grades_for_a_discipline(discipline_id)
        self._save_file()

    def remove_a_grade_for_a_student_at_a_discipline(self, student_id, discipline_id, grade_value):
        super(GradeBinFileRepository, self).remove_a_grade_for_a_student_at_a_discipline(student_id, discipline_id, grade_value)
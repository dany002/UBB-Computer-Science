from repository.StudentRepository import StudentRepository
import pickle
import os.path

class StudentBinFileRepository(StudentRepository):
    def __init__(self, file_name):
        super().__init__()

        self.__file_name = file_name
        if not os.path.exists(self.__file_name):
            self._save_file()
        self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "rb")
        self._students = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._students, file)
        file.close()

    def add_a_student(self, student_that_is_going_to_be_added):
        super(StudentBinFileRepository, self).add_a_student(student_that_is_going_to_be_added)
        self._save_file()

    def remove_a_student(self, student_id):
        super(StudentBinFileRepository, self).remove_a_student(student_id)
        self._save_file()

    def update_a_student_by_name(self, student_name, new_student_id):
        super(StudentBinFileRepository, self).update_a_student_by_name(student_name, new_student_id)
        self._save_file()

    def update_a_student_by_id(self, student_id, new_student_name):
        super(StudentBinFileRepository, self).update_a_student_by_id(student_id, new_student_name)
        self._save_file()
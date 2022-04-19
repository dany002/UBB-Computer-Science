from domain.Student import Student
from domain.Validators import StudentIdError, StudentValidator
from Utils.Utils import Utils

class StudentsService:
    def __init__(self, student_repository, grade_repository):
        self.__repository = student_repository
        self.__grade_repository = grade_repository

    def add_a_student(self, student_id, name):
        """
        It adds a student to the student repository.
        :param student_id: string
        :param name: string
        :return: none
        """

        if student_id.isdigit() == False:
            raise StudentIdError("Student id must be a positive integer.")
        StudentValidator.validate(student_id, name) 
        self.__repository.add_a_student(Student(int(student_id), name))


    def search_a_student_by_student_ID(self, student_id):
        """
        It searches a student by id in the student repository.
        :param student_id: string
        :return: list.
        """
        if student_id.isdigit() == False:
            raise StudentIdError("Student id must be a positive integer.")
        return self.__repository.search_a_student_by_student_ID(student_id)

    def search_a_student_by_name(self, student_name):
        """
        It searches a student by name in the student repository.
        :param student_name: string
        :return: list.
        """
        return Utils.filter(self.__repository.list_of_students(), lambda student: student.name.lower().find(student_name.lower()) != -1)




    def update_a_student_by_id(self, student_id, new_student_name):
        """
        It updates a student by id in the student repository.
        :param student_that_is_going_to_be_updated: string
        :param new_student_id: string
        :return: none
        """
        self.__repository.update_a_student_by_id(student_id, new_student_name)

    def update_a_student_by_name(self, student_name, new_student_id):
        """
        It updates a student by name in the student repository.
        :param new_student_name: string
        :param student_id_that_is_going_to_be_updated: string
        :return: none
        """
        self.__repository.update_a_student_by_name(student_name, int(new_student_id))


    def remove_a_student(self, student_id):
        """
        It removes a student in the student repository using student_id and also it removes all the grades for that student.
        :param student_id: string
        :return: none
        """
        self.__grade_repository.remove_grades_for_a_student(int(student_id))
        self.__repository.remove_a_student(int(student_id))


    def list_of_students(self):
        """
        It return the list of students from the students repository.
        :return: self.__repository.list_of_students()
        """
        return self.__repository.list_of_students()


    def get_index_of_students_list(self, index):
        """
        It return the index-th element from the student list from the students repository.
        :param index: integer
        :return: self.__repository.get_index_of_students_list(index)
        """
        return self.__repository.get_index_of_students_list(index)


    def length_of_students(self):
        """
        It return the length of students from the student list from the students repository.
        :return: self.__repository.length_of_students()
        """
        return self.__repository.length_of_students()


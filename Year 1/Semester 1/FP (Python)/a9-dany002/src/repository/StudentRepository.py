from repository.RepositoryException import RepositoryException, RepositoryException2

class StudentRepository:
    def __init__(self):
        self._students = []


    def add_a_student(self, student_that_is_going_to_be_added):
        """
        It adds a student in the list.
        :param student_that_is_going_to_be_added: Student
        :return: none
        """
        for index in range(len(self._students)):
            if self._students[index].student_id == student_that_is_going_to_be_added.student_id:
                raise RepositoryException("Student ID is not unique.")
        self._students.append(student_that_is_going_to_be_added)

    def remove_a_student(self, student_id):
        """
        It removes a student from the list.
        :param student_id: string.
        :return:none
        """
        id_found = False
        for index in range(len(self._students)):
            if int(self._students[index].student_id) == int(student_id):
                id_found = True
        if id_found == False:
            raise RepositoryException("Student ID is not found.")

        index = 0
        length = len(self._students)
        while index < length:
            if int(self._students[index].student_id) == int(student_id):
                del self._students[index]
                index -= 1
                length -= 1
            index += 1

    def search_a_student_by_student_ID(self, student_id):

        result_list_with_searched_student = []
        for index in range(len(self._students)):
            if int(self._students[index].student_id) == int(student_id):
                student = self._students[index]
                result_list_with_searched_student.append(student)

        if result_list_with_searched_student == []:
            raise RepositoryException("Student id wasn't found.")
        return result_list_with_searched_student

    def search_a_student_by_name(self, student_name):
        """
        It searches a student by student name and it creates a new list result_list_with_searched_student: [{'id': id, 'name': name}, {'id': id, 'name': name2}, ...]
        :param student_name: string
        :return: result_list_with_searched_student, list of dictionaries.
        """
        if student_name.isalpha() == False:
            raise RepositoryException2("Student name has to contain only letters.")
        result_list_with_searched_student = []
        for index in range(len(self._students)):
            if self._students[index].name == student_name:
                student = {'id': self._students[index].student_id, 'name': self._students[index].name}
                result_list_with_searched_student.append(student)
        if result_list_with_searched_student == []:
            raise RepositoryException("Student name wasn't found.")
        return result_list_with_searched_student

    def update_a_student_by_name(self, student_name, new_student_id):
        """
        It updates a student by name and it assign the new_student_id to the student name that was given.
        :param student_name: string
        :param new_student_id: integer.
        :return: none
        """
        for index in range(len(self._students)):
            if self._students[index].student_id == int(new_student_id):
                raise RepositoryException("Student ID is already taken.")

        name_found = False
        for index in range(len(self._students)):
            if self._students[index].name == student_name:
                self._students[index].student_id = new_student_id
                name_found = True
        if name_found == False:
            raise RepositoryException2("There is no name to be updated.")


    def update_a_student_by_id(self, student_id, new_student_name):
        """
        It updates a student by id and it assign the new_student_name to the student id that was given.
        :param student_id: string
        :param new_student_name: string
        :return: none
        """
        id_found = False
        for index in range(len(self._students)):
            if int(self._students[index].student_id) == int(student_id):
                self._students[index].name = new_student_name
                id_found = True
        if id_found == False:
            raise RepositoryException("The given id is not in the list of students.")

    def list_of_students(self):
        """
        It returns the list of students from repository.
        :return: self.__students - list
        """
        return self._students

    def length_of_students(self):
        """
        It returns the length of students from repository.
        :return: len(self.__students) - integer.
        """
        return len(self._students)

    def get_index_of_students_list(self, index):
        """
        It returns the index-th element from the students' list
        :param index: integer
        :return: self.__students[index], element from the students' list.
        """
        return self._students[index]

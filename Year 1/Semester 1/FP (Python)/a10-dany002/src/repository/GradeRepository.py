from Utils.CustomIterable import CustomIterable


class GradeRepository:
    def __init__(self):
        self._grades = CustomIterable()


    def add_a_grade_for_a_student(self, grade_that_is_going_to_be_added):
        """
        It adds a grade in the list.
        :param grade_that_is_going_to_be_added: object
        :return: none
        """

        self._grades.append(grade_that_is_going_to_be_added)


    def remove_grades_for_a_student(self, student_id):
        """
        It removes grades for a given student
        :param student_id: string
        :return: none
        """
        index = 0
        length = len(self._grades)
        while index < length:
            if int(self._grades[index].student_id) == int(student_id):
                del self._grades[index]
                index -= 1
                length -= 1
            index += 1


    def remove_grades_for_a_discipline(self, discipline_id):
        """
        It removes grades for a given discipline.
        :param discipline_id: string
        :return: none
        """
        index = 0
        length = len(self._grades)
        while index < length:
            if int(self._grades[index].discipline_id) == int(discipline_id):
                del self._grades[index]
                index -= 1
                length -= 1
            index += 1

    def remove_a_grade_for_a_student_at_a_discipline(self, student_id, discipline_id, grade_value):
        index = 0
        length = len(self._grades)
        while index < length:
            if int(self._grades[index].discipline_id) == int(discipline_id):
                if int(self._grades[index].student_id) == int(student_id):
                    if int(self._grades[index].grade_value) == int(grade_value):
                        del self._grades[index]
                        index -= 1
                        length -= 1
            index += 1

    def list_of_grades(self):
        """
        It return the list of grades.
        :return: self.__grades
        """
        return [grade for grade in self._grades]

    def length_of_grades(self):
        """
        It return the length of list of grades.
        :return: len(self.__grades)
        """
        return len(self._grades)

    def get_index_of_grades_list(self, index):
        """
        It return the index-th element from the grades list.
        :param index: integer
        :return: self.__grades[index]
        """
        return self._grades[index]

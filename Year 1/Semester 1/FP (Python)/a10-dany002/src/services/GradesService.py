from domain.Grade import Grade
from domain.Validators import GradeError, StudentIdError, DisciplineIdError, StudentIdNotFoundError, \
    DisciplineIdNotFoundError, GradeValidator
from Utils.Utils import Utils


class GradesService:
    def __init__(self, student_repository, disciplines_repository, grades_repository):
        self.__repository = grades_repository
        self.__students_repository = student_repository
        self.__disciplines_repository = disciplines_repository

    def get_all_grades_for_a_given_student(self, student_id):
        grades_for_a_given_student = []
        for index in range(self.__repository.length_of_grades()):
            if int(self.__repository.get_index_of_grades_list(index).student_id) == int(student_id):
                grades_for_a_given_student.append(self.__repository.get_index_of_grades_list(index))
        return grades_for_a_given_student

    def get_all_grades_for_a_given_discipline(self, discipline_id):
        grades_for_a_given_discipline = []
        for index in range(self.__repository.length_of_grades()):
            if int(self.__repository.get_index_of_grades_list(index).discipline_id) == int(discipline_id):
                grades_for_a_given_discipline.append(self.__repository.get_index_of_grades_list(index))
        return grades_for_a_given_discipline

    def add_a_grade(self, student_id, discipline_id, grade_value):
        """
        It adds a grade for a given student id, discipline id and the grade. And also it checks if the given data is valid.
        :param student_id: string
        :param discipline_id: string
        :param grade_value: string
        :return: none
        """

        if grade_value.isdigit() == False:
            raise GradeError("Grade must be a positive integer.")
        if student_id.isdigit() == False:
            raise StudentIdError("Student id must be a positive integer.")
        if discipline_id.isdigit() == False:
            raise DisciplineIdError("Discipline id must be a positive integer.")

        GradeValidator.validate(student_id, discipline_id, grade_value)

        student_id_found = False
        discipline_id_found = False
        for index in range(self.__students_repository.length_of_students()):
            if int(self.__students_repository.get_index_of_students_list(index).student_id) == int(student_id):
                student_id_found = True
        for index in range(self.__disciplines_repository.length_of_disciplines()):
            if int(self.__disciplines_repository.get_index_of_disciplines_list(index).discipline_id) == int(discipline_id):
                discipline_id_found = True

        if student_id_found == False:
            raise StudentIdNotFoundError("Student id wasn't found.")
        if discipline_id_found == False:
            raise DisciplineIdNotFoundError("Discipline id wasn't found.")
        self.__repository.add_a_grade_for_a_student(Grade(int(student_id), int(discipline_id), int(grade_value)))

    def remove_a_grade_for_a_student_at_a_discipline(self, student_id, discipline_id, grade_value):
        self.__repository.remove_a_grade_for_a_student_at_a_discipline(student_id, discipline_id, grade_value)

    def remove_grades_for_a_student(self, student_id):
        """
        It removes the grades for a student from the grade repository.
        :param student_id: string
        :return: none
        """
        self.__repository.remove_grades_for_a_student(student_id)

    def remove_grades_for_a_discipline(self, discipline_id):
        """
        It removes the grades for a discipline from the grade repository.
        :param discipline_id: string
        :return: none
        """
        self.__repository.remove_grades_for_a_discipline(discipline_id)

    ######################### STATISTICS ##################################
    def statistics_for_all_students_failing_at_one_or_more_disciplines(self):
        new_list_with_the_students_that_failed = []
        for index in range(self.__repository.length_of_grades()):
            if int(self.__repository.get_index_of_grades_list(index).grade_value) < 5:
                new_list_with_the_students_that_failed.append(self.__repository.get_index_of_grades_list(index).student_id)
        return new_list_with_the_students_that_failed

    def compute_aggregated_average_for_a_student_at_a_given_discipline(self, student_id, discipline_id):
        sum_of_grades_for_a_student = 0
        number_of_grades_for_a_student = 0
        for index in range(self.__repository.length_of_grades()):
            if int(self.__repository.get_index_of_grades_list(index).student_id) == int(student_id):
                if int(self.__repository.get_index_of_grades_list(index).discipline_id) == int(discipline_id):
                    sum_of_grades_for_a_student += self.__repository.get_index_of_grades_list(index).grade_value
                    number_of_grades_for_a_student += 1
        if number_of_grades_for_a_student != 0:
            return sum_of_grades_for_a_student / number_of_grades_for_a_student
        else:
            return 0

    def compute_aggregated_average_for_a_student(self, student_id):
        sum_of_all_grades_for_a_discipline = 0
        list_of_all_the_disciplines_for_a_student = self.all_the_disciplines_with_at_least_one_grade_for_a_specific_student(student_id)
        for index in range(len(list_of_all_the_disciplines_for_a_student)):
            sum_of_all_grades_for_a_discipline += self.compute_aggregated_average_for_a_student_at_a_given_discipline(student_id, list_of_all_the_disciplines_for_a_student[index])
        if len(list_of_all_the_disciplines_for_a_student) != 0:
            return sum_of_all_grades_for_a_discipline / len(list_of_all_the_disciplines_for_a_student)
        else:
            return 0

    def all_the_disciplines_with_at_least_one_grade_for_a_specific_student(self, student_id):
        new_list_with_all_the_disciplines_with_at_least_one_grade_for_a_student = []
        for index in range(self.__repository.length_of_grades()):
            if int(self.__repository.get_index_of_grades_list(index).student_id) == int(student_id):
                new_list_with_all_the_disciplines_with_at_least_one_grade_for_a_student.append(self.__repository.get_index_of_grades_list(index).discipline_id)
        return list(set(new_list_with_all_the_disciplines_with_at_least_one_grade_for_a_student))

    def all_students_that_have_at_least_a_grade(self):
        new_list_with_all_students_that_have_at_least_a_grade = []
        for index in range(self.__repository.length_of_grades()):
            new_list_with_all_students_that_have_at_least_a_grade.append(self.__repository.get_index_of_grades_list(index).student_id)
        return list(set(new_list_with_all_students_that_have_at_least_a_grade))

    def statistics_for_students_with_best_school_situation(self):
        return Utils.shellSort(self.all_students_that_have_at_least_a_grade(), lambda first_student, second_student: 1
        if self.compute_aggregated_average_for_a_student(first_student) < self.compute_aggregated_average_for_a_student(second_student)
        else (0 if self.compute_aggregated_average_for_a_student(first_student) == self.compute_aggregated_average_for_a_student(second_student)
              else -1))


    def all_disciplines_that_have_at_least_a_grade(self):
        new_list_with_all_disciplines_that_have_at_least_a_grade = []
        for index in range(self.__repository.length_of_grades()):
            new_list_with_all_disciplines_that_have_at_least_a_grade.append(self.__repository.get_index_of_grades_list(index).discipline_id)
        return list(set(new_list_with_all_disciplines_that_have_at_least_a_grade)) # unique discipline id.



    def compute_average_grade_for_a_discipline(self, discipline_id):
        sum_of_grades_for_a_discipline = 0
        number_of_students_for_the_given_discipline = 0
        for index in range(self.__repository.length_of_grades()):
            if int(self.__repository.get_index_of_grades_list(index).discipline_id) == int(discipline_id):
                sum_of_grades_for_a_discipline += self.__repository.get_index_of_grades_list(index).grade_value
                number_of_students_for_the_given_discipline += 1
        if number_of_students_for_the_given_discipline != 0:
            average_grade_for_a_discipline = sum_of_grades_for_a_discipline / number_of_students_for_the_given_discipline
        else:
            return 0
        return average_grade_for_a_discipline

    def statistics_for_all_disciplines_with_at_least_one_grade(self):
        return Utils.shellSort(self.all_disciplines_that_have_at_least_a_grade(), lambda first_discipline, second_discipline: 1
        if self.compute_average_grade_for_a_discipline(first_discipline) < self.compute_average_grade_for_a_discipline(second_discipline)
        else (0 if self.compute_average_grade_for_a_discipline(first_discipline) == self.compute_average_grade_for_a_discipline(second_discipline) else -1))


    def list_of_grades(self):
        """
        It return the list of grades from the grade repository.
        :return: self.__repository.list_of_grades()
        """
        return self.__repository.list_of_grades()

    def length_of_grades(self):
        """
        It return the length of grades list from the grade repository.
        :return: self.__repository.length_of_grades()
        """
        return self.__repository.length_of_grades()

    def get_index_of_grades_list(self, index):
        """
        It return the index-th element from the grades list from grade repository.
        :param index: integer
        :return: self.__repository.get_index_of_grades_list(index)
        """
        return self.__repository.get_index_of_grades_list(index)